from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'showtime', 'seat', 'price')
    list_display_links = ('id', 'user')
    list_filter = ('user', 'showtime')
    search_fields = ('user', 'showtime')
    list_per_page = 25

admin.site.register(Ticket, TicketAdmin)