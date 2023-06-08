from rest_framework import serializers

from .models import SEA_Book, SEA_Booksss


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEA_Book
        fields = ("pk", "book_name", "author",
                  "publishing_house", "ISBN", "Abstract")


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = SEA_Booksss
        fields = ("pk", "id", "book_name", "author",
                  "publishing_house", "ISBN", "Abstract")
