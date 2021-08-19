from django.contrib import admin
from api.models import *

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["id","link","short_link","visit_count"]
    readonly_fields = ["visit_count","random_string"]
    search_fields = ["link","random_string"]
