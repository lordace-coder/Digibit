from django.urls import path
from . import views

urlpatterns = [
    path('',views.CreateReservation.as_view()),
]
