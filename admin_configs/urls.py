from . import views
from django.urls import path

urlpatterns = [
    path('create-bot/',views.CreateMiningBot.as_view(),name='create_bot'),
    path('profiles/',views.CheckProfilesView.as_view(),name='profiles')
]