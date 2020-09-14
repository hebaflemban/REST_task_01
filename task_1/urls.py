
from django.contrib import admin
from django.urls import path
from flights import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', api_views.FlightsList.as_view(), name = 'flights-list' ),
    path('bookings/', api_views.Bookings.as_view(), name = 'bookings-list' )
]
