
from django.urls import path

from booking_v2.views import SignUpView,BookingCreateListView

urlpatterns = [

    path('signup/',SignUpView.as_view()),
    path('bookings/',BookingCreateListView.as_view()),
]