from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name="about_us"),
    path('aci_history', views.aci_history, name="aci_history"),
    path('aci_vmgo', views.aci_vmgo, name="aci_vmgo"),

]
