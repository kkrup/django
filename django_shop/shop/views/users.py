from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers.users import UserSerializer


class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    @staticmethod
    def get(request):
        message = {"user": request.user.username}
        return Response(message)
