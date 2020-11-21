from rest_framework import views, status
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication


class LoginView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'wrong credentials'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        return Response('koko')
