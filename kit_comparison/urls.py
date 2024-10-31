from django.urls import path

from . import views

app_name = "kit_comparison"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("kits/<int:pk>/", views.KitDetailView.as_view(), name="kit_detail"),
    path("lenses/<int:pk>/", views.LensDetailView.as_view(), name="lens_detail"),
]
