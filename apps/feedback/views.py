from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework import generics
from apps.cinemas.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class FeedbackListView(generics.ListCreateAPIView):
    """
    List all feedbacks or create a new feedback.
    
    Use this endpoint to retrieve a list of all feedbacks or create a new feedback if you are a user.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a feedback instance.
    
    Use this endpoint to retrieve, update or delete a feedback instance.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class CreateFeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)