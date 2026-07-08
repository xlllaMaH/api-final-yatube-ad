from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls.jwt')),
]
