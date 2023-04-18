# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from Book.serializers import BookSerializer
from .models import BOOK
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size=20

# class BookList(generics.ListAPIView):
#     queryset = BOOK.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [AllowAny]
#     pagination_class = PageNumberPagination


class BookList(APIView):
    permission_classes = [AllowAny]
    pagination_class = CustomPageNumberPagination

    def get(self, request):
        books = BOOK.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(books, request)
        if page is not None:
            serializer = BookSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)