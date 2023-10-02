from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from games.views import (
    MapsViewset , 
    CharacterViewSet,
    GameReqimeViewSet
)


router = DefaultRouter()
router.register(r'maps', MapsViewset,basename='maps')
router.register(r'characters', CharacterViewSet,basename='characters')
router.register(r'game_regimes', GameReqimeViewSet,basename='game_regimes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include(router.urls))
]
