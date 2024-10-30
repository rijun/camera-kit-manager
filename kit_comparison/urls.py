from django.urls import path

from . import views

app_name = "kit_comparison"
urlpatterns = [
    path("", views.index, name="index"),
    path("kits/<int:kit_id>/", views.kit_detail, name="kit_detail"),
    path("lenses/", views.lenses, name="lenses"),
    path("lenses/<int:lens_id>/", views.lens_detail, name="lens_detail"),
]
