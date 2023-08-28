from django.urls import path
from .views import CreateMovieView, MovieListView, MovieDetailView, DeleteMovieView

urlpatterns = [
    path('', MovieListView.as_view()), # api/movies/
    path('create/', CreateMovieView.as_view()), # api/movies/create/
    path('<int:pk>/', MovieDetailView.as_view()), # api/movies/1/
    path('<int:pk>/delete/', DeleteMovieView.as_view()), # api/movies/1/delete/
]