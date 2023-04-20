# from rest_framework import generics
from django.http import HttpRequest #HTTP 요청을 나타내는 클래스입니다.

from rest_framework.views import APIView 
#위 APIView를 사용하면 HTTP 요쳥 메서드(GET,POST,PUT,DELETE 등)에 대한 적절한 처리기 메서드
# 메서드(get(), post(), put(), delete() 등)를 정의할 수 있습니다

from rest_framework.response import Response
# HTTP 응답을 생성하 데 사용되는 클래스입니다.

from .serializers import BookSerializer
from .models import BOOK

from rest_framework.permissions import AllowAny
# 인증 및 권한 검사를 건너뛰고 모든 사용자가 API 엔드포인트를 사용할 수 있도록 하는 권한 클래스입니다.

# 아래 클래스는 페이지 번호 및 페이지 크기를 기반으로 데이터를 자동으로 분할하고, 페이지네이션을 수행하는 데 
# 필요한 모든 메서드와 속성을 제공합니다.
from rest_framework.pagination import PageNumberPagination

from rest_framework import generics
from rest_framework.filters import SearchFilter

class CustomPageNumberPagination(PageNumberPagination):
    page_size=20



# def로 변환
class BookList(APIView):
    # 모든 사용자가 API 엔드포인트에 접근할 수 있도록 권한을 설정합니다.
    permission_classes = [AllowAny]
    
    # 페이지네이션을 위해 CustomPageNumberPagination 클래스를 사용합니다.
    pagination_class = CustomPageNumberPagination

    def get(self, request:HttpRequest) -> Response:
        # 모든 책 데이터를 가져옵니다.
        books = BOOK.objects.all()
        
        # 페이지네이션 객체를 만듭니다.
        paginator = self.pagination_class()
        
        # 요청된 페이지 번호를 가져옵니다.
        page = request.GET.get('page')
        
        # 페이지 번호가 전달된 경우에는 해당 페이지의 데이터를 가져오고, 아니면 모든 데이터를 가져옵니다.
        if page is not None:
            # 해당 페이지의 데이터를 가져옵니다.
            page_books = paginator.paginate_queryset(books, request)
            
            # 책 데이터를 직렬화합니다.
            serializer = BookSerializer(page_books, many=True)
            
            # 페이지네이션된 응답을 반환합니다.
            return paginator.get_paginated_response(serializer.data)
        
        # 모든 데이터를 가져온 경우에는 직렬화된 책 데이터를 반환합니다.
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookListAPIView(generics.ListAPIView):
    queryset = BOOK.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['Title', 'Author', 'Publisher']