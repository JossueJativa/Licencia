from django.urls import path
from . import views

app_name = "Licencia"

urlpatterns = [
    path('', views.intro, name='intro'),
]