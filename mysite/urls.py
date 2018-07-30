from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name="home"),
	path('prices/',views.prices, name="prices"),
	path('prices2/',views.prices2, name="prices2"),
]