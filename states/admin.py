from django.contrib import admin

from .models import State


# Register your models here.


@admin.register(State)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title',)
    search_fields = ('name',)
    list_per_page = 20

# Register your models here.
