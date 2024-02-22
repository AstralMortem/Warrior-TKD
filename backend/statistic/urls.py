from django.urls import path,include
from . import views

app_name = "statistic"
urlpatterns = [
    path('',views.index, name="index")
]