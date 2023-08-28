from django.urls import path
from .views import *


urlpatterns = [
    path('', CinemaListView.as_view()), # api/v1/cinemas/
    path('<int:pk>/', CinemaDetailView.as_view()), # api/v1/cinemas/1/
    path('<int:pk>/rooms/', CinemaRoomListView.as_view()), # api/v1/cinemas/1/rooms/
    path('<int:pk>/rooms/<int:room_pk>/seats/', CinemaRoomSeatListView.as_view()), # api/v1/cinemas/1/rooms/1/seats/
    path('<int:pk>/rooms/<int:room_pk>/showtimes/', CinemaRoomShowtimeListView.as_view()), # api/v1/cinemas/1/rooms/1/showtimes/
    path('<int:pk>/showtime/<int:showtime_pk>', CinemaShowtimeDetailView.as_view()), # api/v1/cinemas/1/showtimes/
    path('<int:pk>/showtimes/', CinemaShowTimeListView.as_view()), # api/v1/cinemas/1/showtimes/
    path('<int:pk>/create_showtime/', CinemaCreateShowtimeView.as_view()), # api/v1/cinemas/1/create_showtime/
]