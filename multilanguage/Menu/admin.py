from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    list_display = ("name", "link")
    list_display_links =("name", "link")