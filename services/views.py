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




class TransferAPiView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        pass

# views for streaming

# message streaming function
def my_stream():
    mined_total = 0
    times_left = 10
    cool_down = 10
    data = dict()

    while times_left > 1:
        tokens = randrange(1,5)/100
        mined_total += tokens
        data['tokens'] = tokens
        data['mined_total'] = mined_total
        times_left -=1
        yield "\ndata: {}\n\n".format(data)
        time.sleep(cool_down)


# main view
class BotMiningView(views.APIView):
    def get(self,request,*args,**kwargs):
        event_stream = StreamingHttpResponse(my_stream(),content_type = 'text/event-stream',status = 200)
        return event_stream
streamingMessage = BotMiningView.as_view()