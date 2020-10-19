from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

import django
from corsheaders.defaults import default_headers
from ..serializers.users import UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = serializer.save()
        except django.db.utils.IntegrityError as err:
            return Response(
                {"error": str(err)},
                status=status.HTTP_400_BAD_REQUEST)
        else:

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "status": "User created",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                headers=default_headers)
