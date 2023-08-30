from .models import Ticket
from .serializers import TicketSerializer, CreateTicketSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.cinemas.models import Showtime, Seat
from rest_framework.response import Response
from rest_framework import status
from apps.cinemas.permissions import IsOwner, IsAdminOrReadOnly
from rest_framework.exceptions import ValidationError


class MyTicetsListView(generics.ListAPIView):
    """
    List all tickets of the current user.
    
    Use this endpoint to retrieve a list of all tickets of the current user.
    """
    serializer_class = TicketSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        queryset = Ticket.objects.filter(user=self.request.user)
        return queryset


# def create_order_for_user(user):
#     cart = Cart.objects.get(user=user)
#     total_price = sum([item.product_variant.product.price * item.quantity for item in cart.items.all()])

#     if total_price > 20000:
#         discount = total_price * 0.1
#         total_price -= discount

#     order = Order.objects.create(user=user, total_price=total_price, status='Pending')

#     for cart_item in cart.items.all():
#         OrderItem.objects.create(
#             order=order,
#             product_variant=cart_item.product_variant,
#             quantity=cart_item.quantity,
#             price=cart_item.product_variant.product.price * cart_item.quantity
#         )

#     cart.items.all().delete()

#     return order


# class CreateOrderView(generics.CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def create(self, request, *args, **kwargs):
#         user = self.request.user

#         if user.cart.cart_items.count() == 0:
#             return Response({'error': 'Your cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

#         order = create_order_for_user(user)

#         serializer = self.get_serializer(order)
#         if check_user_address(request):
#             return Response({'error': 'You must have at least one address'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


def create_ticket_for_user(user, showtime_id, seat_id, price):
    try:
        showtime = Showtime.objects.get(id=showtime_id)
        room = showtime.room
        if not Seat.objects.filter(room=room, id=seat_id).exists():
            raise ValidationError('Seat is not in this room')
        book_seat = Seat.objects.get(id=seat_id)
        if book_seat.is_taken:
            raise ValidationError('Seat is already taken')
        book_seat.is_taken = True
        book_seat.save()
        ticket = Ticket.objects.create(user=user, showtime=showtime, seat=book_seat, price=price)
        return ticket

    except Showtime.DoesNotExist:
        raise ValidationError('Showtime does not exist')
    


class CreateTicketView(generics.CreateAPIView):
    """
    Create a ticket for the current user.
    
    Use this endpoint to create a ticket for the current user.
    """
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        showtime_id = request.data.get('showtime')
        seat_id = request.data.get('seat')
        price = request.data.get('price')
        if not showtime_id or not seat_id or not price:
            return Response({'error': 'You must provide showtime, seat and price'}, status=status.HTTP_400_BAD_REQUEST)
        ticket = create_ticket_for_user(user, showtime_id, seat_id, price)
        serializer = self.get_serializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)