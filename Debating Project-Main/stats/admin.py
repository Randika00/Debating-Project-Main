from django.contrib import admin
from .models import Tournament, Debater, Institution, User, Motion, Round, Score
from stats import models
# Register your models here.


class Debateradmin(admin.ModelAdmin):
    list_display = ("id", "name", "institution")


class Ins_admin(admin.ModelAdmin):
    list_display = ("id", "name", "code")


class T_admin(admin.ModelAdmin):
    list_display = ("name", "slug", "organizer", "teamno", "timestamp")


class MotionAdmin(admin.ModelAdmin):
    list_display = ("motion", "infoslide", "theme")


class ScoreAdmin(admin.ModelAdmin):
    list_display = ("round", "speaker", "score")


admin.site.register(Debater, Debateradmin)
admin.site.register(Institution, Ins_admin)
admin.site.register(User)
admin.site.register(Tournament, T_admin)
admin.site.register(Round)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Motion, MotionAdmin)
