from rest_framework import serializers
from .models import BOOK

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOOK
        fields = '__all__'
