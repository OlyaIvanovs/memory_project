from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ['first_side_text', 'second_side_text', 'show_date', 'value']


admin.site.register(Card, CardAdmin)

