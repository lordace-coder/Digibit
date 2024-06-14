from rest_framework import generics,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from custom_auth.models import CustomUser
from rest_framework.permissions import IsAuthenticated
import json
from random import randrange
import time
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from api.models import MiningBot,Profile,Wallet
from api.serializers.serializers import ProfileSerializer
from services.serializers import MiningBotSerializer
from decimal import Decimal

class TransferAPiView(views.APIView):
    """
        View for sending crypton to other addresses or emails
    """
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        pass

# views for streaming

# message streaming function
def my_stream(bot:MiningBot,profile:Profile):
    mined_total = 0
    times_left = 10
    cool_down = bot.cool_down_time
    data = dict()

    while times_left > 1:
        tokens = randrange(1,5)/100 #replace with bots mine range
        bot.hp = bot.hp - Decimal(randrange(1,3)/8)
        bot.save()
        mined_total += tokens
        data['tokens'] = tokens
        data['mined_total'] = mined_total
        times_left -=1
        yield "\ndata: {}\n\n".format(data)
        time.sleep(cool_down)
    profile.wallet.credit(data.get('mined_total'))


# main view
class BotMiningView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MiningBot.objects.all()
    serializer_class = MiningBotSerializer

    def get(self,request,*args,**kwargs):
        user_profile = Profile.objects.get(user=request.user)

        # TODO CHECK IF THE REQUESTED BOT EXISTS
        bot_id = kwargs.get('id')
        print(len(bot_id),len(user_profile.bots.all()[0].id))
        bot  = user_profile.bots.filter(id=bot_id)
        if bot.exists():
            bot = bot[0]
            if not bot.hp > 0:#check if bot is still useable
                return Response(status=404)
            # todo PASS IN THE USERS WALLET INTO THE STREAM AND ALSO THE BOT IN USE
            event_stream = StreamingHttpResponse(my_stream(bot,user_profile),content_type = 'text/event-stream',status = 200)
            return event_stream
        return Response({'error':'bot does not exist'},status=404)
streamingMessage = BotMiningView.as_view()


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.queryset.get(user = self.request.user)
