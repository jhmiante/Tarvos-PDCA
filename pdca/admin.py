from django.contrib import admin

from .models import PDCA, PDCAItem


# Register your models here.
@admin.register(PDCA)
class PDCAAdmin(admin.ModelAdmin):
    list_display = ('objetivo', 'usuario')


@admin.register(PDCAItem)
class PDCAItemAdmin(admin.ModelAdmin):
    list_display = ('pdca', 'data')
