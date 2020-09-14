from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer
from rest_framework.generics import ListAPIView
import datetime
from django.utils import timezone


class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class Bookings(ListAPIView):
    queryset = Booking.objects.filter(date__gt = datetime.date.today() )
    serializer_class = BookingSerializer
