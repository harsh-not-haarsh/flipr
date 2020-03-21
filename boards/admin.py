from django.contrib import admin
from .models import PersonalBoard, TeamBoard


class PersonalBoardAdmin(admin.ModelAdmin):
    class Meta:
        model = PersonalBoard


admin.site.register(PersonalBoard, PersonalBoardAdmin)


class TeamBoardAdmin(admin.ModelAdmin):
    class Meta:
        model = TeamBoard


admin.site.register(TeamBoard, TeamBoardAdmin)
