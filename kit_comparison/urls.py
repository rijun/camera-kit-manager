from django.urls import path

from . import views

app_name = "kit_comparison"
urlpatterns = [
    path("", views.index, name="index"),
    path("kits/<int:pk>", views.KitDetailView.as_view(), name="kit_detail"),
    path("kits/new", views.KitCreateView.as_view(), name="kit_create"),
    path("kits/<int:pk>/edit", views.KitUpdateView.as_view(), name="kit_update"),
    path("lenses/", views.LensListView.as_view(), name="lens_list"),
    path("lenses/<int:pk>", views.LensDetailView.as_view(), name="lens_detail"),
]
