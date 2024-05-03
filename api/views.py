from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.serializers import UserSerializer,UserDetailSerializer
from custom_auth.models import CustomUser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    refresh_token:RefreshToken = RefreshToken()

    def post(self, request, *args, **kwargs):
        qs =  super().post(request, *args, **kwargs)
        user_data = qs.data
        # ! get user model instance for token generation
        user_obj = CustomUser.objects.get(email = user_data.get('email'))

        # ! GENERATE TOKENS AND APPEND THEM TO RESPONSE DATA
        if user_obj :
            token_pair = self.refresh_token.for_user(user_obj)
            qs.data['refresh'] = str(token_pair)
            qs.data['access'] = str(token_pair.access_token)
        else:
            return Response(status=400)
        return qs


class UserFullControlView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser]