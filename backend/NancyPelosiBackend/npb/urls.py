from django.urls import path
from . import views

urlpatterns = [
    path('populate', views.populateDB, name="populate")
]