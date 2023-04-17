from rest_framework import generics
from Book.serializers import BookSerializer
from .models import BOOK
from rest_framework.permissions import AllowAny

class BookList(generics.ListAPIView):
    queryset = BOOK.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
