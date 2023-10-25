from django.contrib import admin
from .models import Milestone

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'parent', 'description',)
    list_filter = ('user',)