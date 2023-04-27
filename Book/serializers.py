from rest_framework import serializers
from .models import BOOK

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # BookSerializer가 사용할 모델을 지정합니다.
        model = BOOK
        
        # 직렬화할 필드를 모두 지정합니다.
        fields = '__all__'

# Book_search 클래스는 BOOK 모델에서 필요한 필드들을 가져와서 시리얼라이저(serializer)를 만드는 클래스입니다.
class Book_search(serializers.ModelSerializer):
    # 이 클래스는 Meta 클래스 안에서 필드를 정의합니다.
    class Meta:
        model = BOOK
        # 'ID', 'Title', 'Author', 'Publisher', 'Filter_number', 'All_filter', 'Y_date' 필드를 정의하고, 모델과 연결합니다.
        fields = ['ID', 'Title', 'Author', 'Publisher', 'Filter_number', 'All_filter', 'Y_date']
        # 이렇게 정의된 시리얼라이저는 해당 필드들에 대한 검증 및 데이터 변환을 수행할 수 있습니다.