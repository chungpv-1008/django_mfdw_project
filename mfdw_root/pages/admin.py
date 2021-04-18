from django.contrib import admin
from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "update_date")
    ordering = ("title",)
    search_fields = ("title",)

admin.site.register(Page, PageAdmin)
