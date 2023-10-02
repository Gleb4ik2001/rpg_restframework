from rest_framework import serializers
from .models import (
    GameRegime,
    Characters,
    Map
)


class MapSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    choiced_map = serializers.CharField()

class MapCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = [
            'choiced_map'
        ]

class CharactersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    is_premium = serializers.BooleanField()
    img = serializers.ImageField()
    power = serializers.IntegerField()


class CharacterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Characters
        fields = [
            'title',
            'is_premium',
            'img',
            'power'
        ]

class GameRegimeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class GameRegimeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= GameRegime
        fields = [
            'title'
        ]