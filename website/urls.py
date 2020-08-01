from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('about', views.about, name="about"),
	path('generalPractice', views.generalPractice, name="generalPractice"),
	path('womensHealth', views.womensHealth, name="womensHealth"),
	path('OGUK', views.OGUK, name="OGUK"),
	path('employment', views.employment, name="employment"),

	path('appointment', views.appointment, name="appointment"),


	path('occupational', views.occupational, name="occupational"),
	path('seafarers', views.seafarers, name="seafarers"),
	path('cruise', views.cruise, name="cruise"),
	path('contact', views.contact, name="contact"),



]
