from django.conf.urls import url, include
from second_app import views

urlpatterns = [
    url(r'^index/', views.index, name="index"),
    url(r'^help/', views.help, name="help"),
]