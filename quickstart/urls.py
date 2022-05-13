
from django.urls import path, include
from rest_framework import routers

from quickstart import views

app_name = 'quickstart'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]