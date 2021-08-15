import json

from django.views.decorators.http import require_POST
from rest_framework.serializers import Serializer
import stripe
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from stripe import webhook
from stripe.api_resources import line_item

from .models import Order, Billing_address
from .serializers import BillingAddressSerializer, OrderSerailzier, PaymentUserSerializer, OrderDetailSerailzier
from product.models import User_profile
from rest_framework.permissions import IsAuthenticated

from product.models import Subscription_Plan


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerailzier
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerailzier
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class BillingAddressListView(generics.ListAPIView):
    serializer_class = BillingAddressSerializer
    queryset = Billing_address.objects.all()


class BillingAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BillingAddressSerializer
    permission_classes = [IsAuthenticated]
    queryset = Billing_address.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Billing_address.objects.get(pk=instance.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY

    return Response({'pub_key': pub_key})


@api_view(['POST'])
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = request.data
    print(data)
    if data['plan']:
        price_id = 'price_1J8WjoBaL13HgkoyyGzH3ZBo'

    # billing_address = BillingAddressSerializer(data['billing'])
    gateway = data['gateway']
    product_type = data['product_type']
    user_profile = User_profile.objects.get(user__in=[data['user']])
    if gateway == 'stripe':
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=user_profile.user.uid,
                success_url='http://127.0.0.1:8000/payment/success/?session_id={CHECKOUT_SESSION_ID}&success=true',
                cancel_url='http://127.0.0.1:8000/?canceled=true',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1
                    }
                ]
            )
            return Response({'sessionId': checkout_session['id']})
        except Exception as e:
            return Response({'error': str(e)})


@api_view(['POST'])
def create_topup_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = request.data
    print(request.user.id)
    gateway = data['gateway']
    product_type = data['product_type']
    billing_id = create_billing(data['billing_address'])
    order = {
        'user': request.user.id,
        'billing_address': billing_id

    }
    order_info = OrderSerailzier(data=order)
    if order_info.is_valid():
        order_info.save()
        print(order_info.data)
    if gateway == 'stripe' and product_type == 'topup':
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=order_info.data['uuid'],
                success_url="http://localhost:8081/payment/success?session_id={"
                            "CHECKOUT_SESSION_ID}&success=true&order_id=%s" % order_info.data['uuid'],
                cancel_url='http://localhost:8081/?canceled=true',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': data['price_id'],
                        'quantity': 1
                    }
                ]
            )
            current_order = Order.objects.get(uuid=checkout_session['client_reference_id'])
            current_order.payment_intent = checkout_session['payment_intent']
            current_order.paid_amount = checkout_session['amount_total']
            current_order.save()
            print(current_order)
            return Response({'sessionId': checkout_session['id']})
        except Exception as e:
            return Response({'error': str(e)})


def create_billing(billing):
    serializer = BillingAddressSerializer(data=billing)

    if serializer.is_valid():
        serializer.save()
        return serializer.data['id']


@api_view(['POST'])
def check_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    error = ''
    try:
        user_profile = User_profile.objects.get(user__in=[request.user])
        subscription = stripe.Subscription.retrieve(user_profile.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)
        user_profile.plan_status = user_profile.PLAN_ACTIVE
        user_profile.plan_end_date = datetime.fromtimestamp(subscription.current_period_end)
        user_profile.plan = Subscription_Plan.objects.get(title=product.name)
        user_profile.save()

        serializer = PaymentUserSerializer(user_profile)
        print('serializer', serializer)
        return Response(serializer.data)
    except Exception as e:
        error = 'There something wrong. Please try again!'

        return Response({'error': error, 'description': e})


