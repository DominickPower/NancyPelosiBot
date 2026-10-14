from django.urls import path
from . import views

urlpatterns = [
    path('populate', views.populateDB, name="populate"),
    path('reader', views.reader, name="Reader")
]