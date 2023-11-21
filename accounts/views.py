from django.shortcuts import render

# Create your views here.
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class ProfileView(APIView):
  queryset = User.objects
  serializer_class = UserSerializer

  def get(self, request):
    current_user = request.user
    serializer = UserSerializer(current_user)
    print(serializer)
    return Response(serializer.data)