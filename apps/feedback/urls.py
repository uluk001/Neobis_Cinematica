from django.urls import path
from .views import *

urlpatterns = [
    path('', FeedbackListView.as_view(), name='feedback_list'), # /feedback/
    path('create/', CreateFeedbackView.as_view(), name='create_feedback'), # /feedback/create/
    path('<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'), # /feedback/1/
]