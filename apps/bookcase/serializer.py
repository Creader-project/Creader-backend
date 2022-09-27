# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '26/07/2021 17:47'

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from bookitem.serializers import BookSerializer, ChapterDetailSerializer
from .models import Bookcase, BookMark  #


class BookMarkSerializer(serializers.ModelSerializer):
    """
    BookMark serializer
    This serializer is used to serialize the bookmark model
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = BookMark
        fields = '__all__'

    def create(self, validated_data):
        """
        There are three conditions for creating a bookmark:
        1. The user want to mark a chapter
            a. The user has the book in his bookcase
            b. The user does not have the book in his bookcase
        3. The user has bookmarked the chapter, and the bookmark is not the latest
        Create and return a new `Snippet` instance, given the validated data.
        """
        chapter_id_val = validated_data.pop('chapter')
        user_id_val = validated_data.pop('user')
        try:
            exist_book = Bookcase.objects.get(book__pk=chapter_id_val.book_id, user__pk=user_id_val.id)
            print(exist_book)
            if exist_book:
                if exist_book.bookmark is not None:
                    bookmark = BookMark.objects.filter(id=exist_book.bookmark.id).update(chapter_id=chapter_id_val.id,
                                                                                         **validated_data)
                    return {'type': 'update', 'bookmark': bookmark, 'message': 'Bookmark update'}
                else:
                    bookmark = BookMark.objects.create(user_id=user_id_val.id, chapter_id=chapter_id_val.id,
                                                       **validated_data)
                    Bookcase.objects.filter(book__chapter=chapter_id_val.id, user_id=user_id_val.id).update(
                        bookmark_id=bookmark.id)
                    return {'type': 'New Bookmark', 'bookmark': bookmark, 'message': 'Bookmark created'}
        except Exception as e:
            print(e)
        bookmark = BookMark.objects.create(user_id=user_id_val.id, chapter_id=chapter_id_val.id, **validated_data)
        Bookcase.objects.create(user_id=user_id_val.id, book_id=chapter_id_val.book_id, bookmark_id=bookmark.id)
        return {'type': 'New book', 'bookmark': bookmark, 'message': 'Bookmark created and new book added'}


class BookMarkDetailSerializer(serializers.ModelSerializer):
    """
    BookMark detail serializer
    This serializer is used to serialize the bookmark model
    """
    chapter = ChapterDetailSerializer()

    class Meta:
        model = BookMark
        fields = '__all__'


class BookCaseSerializer(serializers.ModelSerializer):
    """
    Bookcase serializer
    This serializer is used to serialize the bookcase model
    This unique together validator is used to check if the user has the book in his bookcase
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Bookcase
        validators = [
            UniqueTogetherValidator(
                queryset=Bookcase.objects.all(),
                fields=('user', 'book'),
                message='Already existing in the bookcase'
            )
        ]

        fields = ('id', 'user', 'book', 'bookmark')
