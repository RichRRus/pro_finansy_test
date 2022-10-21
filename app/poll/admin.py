from django.contrib import admin

from poll import models


class PollOptionInline(admin.TabularInline):
    model = models.PollOption


@admin.register(models.PollOption)
class PollOptionAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [
        PollOptionInline,
    ]


@admin.register(models.PollAnswer)
class PollAnswerAdmin(admin.ModelAdmin):
    ...
