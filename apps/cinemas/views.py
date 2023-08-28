from .models import Cinema, Seat, Showtime, Room
from .serializers import CinemaSerializer, SeatSerializer, RoomSerializer, ShowtimeSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from django.http import Http404
from django.utils import timezone


class CinemaListView(generics.ListCreateAPIView):
    """
    List all cinemas or create a new cinema.

    Use this endpoint to retrieve a list of all existing cinemas or create a new cinema.
    """
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CinemaShowTimeListView(generics.ListCreateAPIView):
    """
    List all showtimes.

    Use this endpoint to retrieve a list of all existing showtimes.

    Parameters:
    - `cinema_id` (int): Id of the cinema.
    """
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        cinema_id = self.kwargs['pk']
        queryset = Showtime.objects.filter(room__cinema_id=cinema_id).filter(start_time__gte=timezone.now())
        return queryset


class CinemaRoomListView(generics.ListCreateAPIView):
    """
    List all rooms or create a new room.

    Use this endpoint to retrieve a list of all existing rooms or create a new room.
    """
    serializer_class = RoomSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        cinema_id = self.kwargs['pk']
        queryset = Room.objects.filter(cinema_id=cinema_id)
        return queryset


class CinemaRoomSeatListView(generics.ListCreateAPIView):
    """
    List all seats or create a new seat.

    Use this endpoint to retrieve a list of all existing seats or create a new seat.

    Parameters:
    - `room_pk` (int): Id of the room.
    """
    serializer_class = SeatSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        room_id = self.kwargs['room_pk']
        room = Room.objects.get(id=room_id)
        queryset = Seat.objects.filter(room=room)
        return queryset


class CinemaRoomShowtimeListView(generics.ListCreateAPIView):
    """
    List all showtimes.

    Use this endpoint to retrieve a list of all existing showtimes.

    Parameters:
    - `room_id` (int): Id of the room.
    """
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        room_id = self.kwargs['room_pk']
        queryset = Showtime.objects.filter(room_id=room_id)
        return queryset


class CinemaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a cinema.
    
    Use this endpoint to retrieve, update or delete a specific cinema identified by its id.

    Parameters:
    - `id` (int): Id of the cinema.
    """
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a room.

    Use this endpoint to retrieve, update or delete a specific room identified by its id.

    Parameters:
    - `id` (int): Id of the room.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CinemaShowtimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a showtime for a specific cinema.

    Use this endpoint to retrieve, update or delete a specific showtime for a cinema identified by its id.

    Parameters:
    - `pk` (int): Id of the cinema.
    - `showtime_pk` (int): Id of the showtime.
    """
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer

    def get_object(self):
        cinema_id = self.kwargs['pk']
        showtime_id = self.kwargs['showtime_pk']
        
        try:
            return Showtime.objects.get(room__cinema_id=cinema_id, pk=showtime_id)
        except Showtime.DoesNotExist:
            raise Http404("Showtime not found")


class CinemaCreateShowtimeView(generics.CreateAPIView):
    """
    Create a new showtime.

    Use this endpoint to create a new showtime.

    Parameters:
    - `room_id` (int): Id of the room.
    - `movie_id` (int): Id of the movie.
    - `start_time` (datetime): Start time of the showtime.
    - `end_time` (datetime): End time of the showtime.
    """
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

    def post(self, request, *args, **kwargs):
        serializer = ShowtimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class CreateRoomView(generics.CreateAPIView):
    """
    Create a new room.

    Use this endpoint to create a new room.

    Parameters:
    - `cinema_id` (int): Id of the cinema.
    - `name` (str): Name of the room.
    - `number` (int): Number of the room.
    - `capacity` (int): Capacity of the room.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)
