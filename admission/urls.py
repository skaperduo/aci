from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission, name="admission"),
    path('confirmation', views.confirmation, name="confirm")
]
