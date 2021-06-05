# djangorestframework를 install 후 직접 파일 생성
# 시리얼라이저 : Python 언어(클래스)를 브라우저가 이해하도록 json형식으로 바꿔줌
from rest_framework import serializers
from .models import WiseSaying


class WiseSayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiseSaying
        fields = '__all__'