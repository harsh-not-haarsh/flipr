from django.contrib import admin
from .models import PersonalBoard, Teamboard


class PersonalBoardAdmin(admin.ModelAdmin):
    class Meta:
        model = PersonalBoard


admin.site.register(PersonalBoard, PersonalBoardAdmin)


class TeamboardAdmin(admin.ModelAdmin):
    class Meta:
        model = Teamboard


admin.site.register(Teamboard, TeamboardAdmin)
