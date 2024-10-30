from django.contrib import admin

from .models import Lens, Kit

class LensAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["manufacturer", "name"]}),
        ("Specifications", {"fields": ["focal_length", "aperture", "weight", "length", "diameter", "filter_size"]}),
    ]

admin.site.register(Lens, LensAdmin)
admin.site.register(Kit)
