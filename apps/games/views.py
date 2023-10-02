from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Map ,
    Characters,
    GameRegime
)
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import(
    MapSerializer,
    MapCreateSerializer,
    CharactersSerializer,
    CharacterCreateSerializer,
    GameRegimeSerializer,
    GameRegimeCreateSerializer
)
from rest_framework.exceptions import ValidationError

class MapsViewset(viewsets.ViewSet):
    queryset = Map.objects.all()
    def list(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        serializer = MapSerializer(
            instance=self.queryset,
            many=True
        )
        return Response(
            data=serializer.data
        )
    def retrieve(
        self,
        request:Request,
        pk:int =None
    )->Response:
        try:
            map = self.queryset.get(id=pk)
        except Map.DoesNotExist:
            raise ValidationError('Map with such ID does not exists',code=404)
        serializer = MapSerializer(instance=map)
        return Response(data=serializer.data)

    def create(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        serializer = MapCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        map : MapCreateSerializer = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'Map {map.choiced_map} has been created!'
            }
        )
    
class CharacterViewSet(viewsets.ViewSet):
    queryset= Characters.objects.all()

    def list(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        character = CharactersSerializer(
            instance=self.queryset,
            many= True
        )
        return Response(
            data=character.data
        )
    def retrieve(
        self,
        request:Request,
        pk:int =None
    )->Response:
        try:
            character = self.queryset.get(id=pk)
        except Characters.DoesNotExist:
            raise ValidationError('Character with such ID does not exists',code=404)
        serializer = CharactersSerializer(instance=character)
        return Response(data=serializer.data)
    
    def create(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        serializer = CharacterCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        character : CharacterCreateSerializer = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'character {character.title} has been created!'
            }
        )
    
class GameReqimeViewSet(viewsets.ViewSet):
    queryset= GameRegime.objects.all()

    def list(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        game_regime = GameRegimeSerializer(
            instance=self.queryset,
            many= True
        )
        return Response(
            data=game_regime.data
        )
    def retrieve(
        self,
        request:Request,
        pk:int =None
    )->Response:
        try:
            game_regime = self.queryset.get(id=pk)
        except GameRegime.DoesNotExist:
            raise ValidationError('Game regime with such ID does not exists',code=404)
        serializer = GameRegimeSerializer(instance=game_regime)
        return Response(data=serializer.data)
    
    def create(
        self,
        request:Request,
        *args:tuple,
        **kwargs:dict
    )->Response:
        serializer = GameRegimeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game_regime : GameRegimeCreateSerializer = serializer.save()
        return Response(
            data={
                'status':'ok',
                'message':f'Game regime {game_regime.title} has been created!'
            }
        )