from django.urls import path
from . import views


urlpatterns = [
    path("", views.estimate_price, name="estimate_price"),
]
