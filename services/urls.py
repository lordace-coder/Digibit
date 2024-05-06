from django.urls import path
from . import views


urlpatterns = [
    path('mine-session/<slug:id>',views.streamingMessage,name="mine"),
    path('profile/',views.ProfileView.as_view()),
]