from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.view_home, name="home"),
    path('about', views.view_home, name="about"),
    path('contact', views.view_home, name="contact"),
    path('vehicles', views.view_vehicles, name="vehicles"),
    path('vehicles/addvehicle', views.view_addvehicle, name="addvehicle"),
    path('vehicles/addvehicle/save', views.save_vehicle, name="create_vehicle"),
    path('vehicles/updatevehicle', views.updatevehicle, name="update"),
    path('vehicles/voided/<uuid:id>', views.voided, name="voided"),
    path('vehicles/unvoided/<uuid:id>', views.unvoided, name="unvoided"),
    
]