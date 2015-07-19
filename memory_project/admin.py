from django.contrib import admin

from .models import Card, TranslateText


class CardAdmin(admin.ModelAdmin):
    list_display = ['first_side_text', 'second_side_text', 'extra_text', 'show_date', 'value']


class TranslateTextAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


admin.site.register(Card, CardAdmin)
admin.site.register(TranslateText, TranslateTextAdmin)