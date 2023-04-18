# from rest_framework import generics
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import BOOK
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size=20

# 이전 코드
# class BookList(generics.ListAPIView):
#     queryset = BOOK.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [AllowAny]
#     pagination_class = PageNumberPagination


# def로 변환
class BookList(APIView):
    permission_classes = [AllowAny]
    pagination_class = CustomPageNumberPagination

    def get(self, request:HttpRequest)->Response:
        books = BOOK.objects.all()
        paginator = self.pagination_class()
        page = request.GET.get('page')
        if page is not None:
            page_books = paginator.paginate_queryset(books, request)
            serializer = BookSerializer(page_books, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)