from rest_framework import serializers
from .models import BOOK

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # BookSerializer가 사용할 모델을 지정합니다.
        model = BOOK
        
        # 직렬화할 필드를 모두 지정합니다.
        fields = '__all__'