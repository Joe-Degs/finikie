from django import views
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from finikie.quickstart.views import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.object.all().order_by('-data-joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = User.object.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]