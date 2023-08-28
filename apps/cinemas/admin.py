from django.contrib import admin
from .models import Cinema, Seat, Showtime, Room


class SeatInline(admin.TabularInline):
    model = Seat
    extra = 0


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email')
    list_filter = ('is_open', 'address')
    search_fields = ('name', 'address', 'phone', 'email')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'cinema', 'capacity', 'is_3d', 'is_vip')
    list_filter = ('cinema', 'is_3d', 'is_vip')
    search_fields = ('name', 'cinema__name')
    inlines = [SeatInline]


class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'room', 'start_time')
    list_filter = ('room', 'movie')
    search_fields = ('movie__title', 'room__name')


admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Showtime, ShowtimeAdmin)
