from .serializers import AccountCreateSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import User
from .serializers import UserListSerializer
from rest_auth.views import LoginView


class AccountCreateView(APIView):
    serializer_class = AccountCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = AccountCreateSerializer(data=request.data)
        response = {}
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            username = serializer.validated_data["email"].split("@")[0]
            User.objects.create_user(username=username, email=email, password=password)
            response["registered"] = True
            return Response(response, status=status.HTTP_200_OK)
        response["registered"] = False
        response["error"] = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(LoginView):
    pass


class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserListSerializer
