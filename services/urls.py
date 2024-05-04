from django.urls import path
from . import views


urlpatterns = [
    path('mine-session',views.streamingMessage)
]