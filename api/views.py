from rest_framework import generics,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.serializers import UserSerializer,UserDetailSerializer
from custom_auth.models import CustomUser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from ace_tokens.models import PasswordTokens
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


class PasswordRecoveryView(views.APIView):
    def get(self,request,*args,**kwargs):
        email = request.GET.get('email')
        if email:
            try:
                # ! CHECK IF ACCOUNT WITH EMAIL EXISTS
                qs = CustomUser.objects.filter(email = email)
                if not qs.exists():
                    return Response({'error':"account with the given mail doesnt exist"},status=404)
                # todo generate recovery token using email and send it to the users email
                PasswordTokens.objects.create(user = qs[0])
                return Response({'data':'Recovery token has succesfully been sent to your email'},status=200)
            except Exception as e:
                return Response({'error':f"error occured [{e}]"},status=400)
        return Response('email cant be empty')