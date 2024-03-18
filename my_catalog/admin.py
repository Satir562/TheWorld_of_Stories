from django.contrib import admin
from .models import Story

@admin.register(Story)
class StorysAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'poster', 'date_publisher', 'publisher')
    list_display_links = ('id', 'title', 'summary')


# admin.site.register(Story,StorysAdmin)
# Register your models here.
