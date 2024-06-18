from rest_framework.generics import CreateAPIView
from .serializers import ReservationSerializer
from rest_framework.response import Response
from .models import Reservation
# from rest_framework import

class CreateReservation(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        if self.queryset.filter(email = request.data.get('email')).exists():
            return Response(data={'error':'This email has already made a reservation'},status=500)
        return super().post(request, *args, **kwargs)