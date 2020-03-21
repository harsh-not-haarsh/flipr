from django.contrib import admin
from .models import Board, List, Card


class BoardAdmin(admin.ModelAdmin):
    class Meta:
        model = Board


admin.site.register(Board, BoardAdmin)


class ListAdmin(admin.ModelAdmin):
    class Meta:
        model = List


admin.site.register(List, ListAdmin)


class CardAdmin(admin.ModelAdmin):
    class Meta:
        model = Card


admin.site.register(Card, CardAdmin)
