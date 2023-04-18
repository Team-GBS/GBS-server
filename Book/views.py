from rest_framework import generics
from Book.serializers import BookSerializer
from .models import BOOK
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size=20

class BookList(generics.ListAPIView):
    queryset = BOOK.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
