from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ansaraconnectapi.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view/edit Users
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view/edit Groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer