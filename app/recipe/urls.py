from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from recipe import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
