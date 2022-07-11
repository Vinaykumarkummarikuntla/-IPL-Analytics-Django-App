"Importing the path"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('played', views.PlayedPerYear,name="matchesplayed"),
    path('won', views.WonPerYear,name='wonperyear'),
    path('runs', views.ExtraRunsin2016 ,name='extraruns'),
    path('bowler', views.EconomicBowler,name='economicbowler'),
]
