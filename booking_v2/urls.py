
from django.urls import path

from booking_v2.views import SignUpView,BookingCreateListView,BookingRetrieveUpdateDelete

urlpatterns = [

    path('signup/',SignUpView.as_view()),
    path('bookings/',BookingCreateListView.as_view()),
    path('bookings/<int:pk>/',BookingRetrieveUpdateDelete.as_view()),
]