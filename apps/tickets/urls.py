from django.urls import path
from .views import CreateTicketView, MyTicetsListView

urlpatterns = [
    path('', MyTicetsListView.as_view()), # /tickets/
    path('create/', CreateTicketView.as_view()), # /tickets/create/
]