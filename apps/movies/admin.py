from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'is_there_at_the_box_office', 'rating', 'genre', 'updated_at')
    list_filter = ('is_there_at_the_box_office', 'genre')
    search_fields = ('title', 'genre')
    date_hierarchy = 'release_date'
    ordering = ('-release_date',)


admin.site.register(Movie, MovieAdmin)