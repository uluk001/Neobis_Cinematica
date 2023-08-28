from .serializers import MovieSerializer
from .models import Movie
from rest_framework import generics
from apps.cinemas.permissions import IsAdminOrReadOnly


class MovieListView(generics.ListCreateAPIView):
    """
    List all movies, or create a new movie.
    
    Use this endpoint to retrieve a list of all existing movies or create a new movie.
    """
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter(is_there_at_the_box_office=True)
        return queryset


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a movie instance.
    
    Use this endpoint to retrieve, update or delete a movie instance.
    
    Parameters:
    - `pk` (int): Id of the movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CreateMovieView(generics.CreateAPIView):
    """
    Create a new movie.
    
    Use this endpoint to create a new movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]


# Withdraw from the box office
class WithdrawMovieView(generics.UpdateAPIView):
    """
    Withdraw a movie from the box office.
    
    Use this endpoint to withdraw a movie from the box office.
    
    Parameters:
    - `pk` (int): Id of the movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]


class DeleteMovieView(generics.DestroyAPIView):
    """
    Delete a movie.
    
    Use this endpoint to delete a movie.
    
    Parameters:
    - `pk` (int): Id of the movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer