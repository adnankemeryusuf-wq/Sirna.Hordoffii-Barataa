from django.urls import path
from . import views

# Hubachiisa: Maqaan kun 'urlpatterns' ta'uu qaba (dhuma irratti 's' qaba)
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]