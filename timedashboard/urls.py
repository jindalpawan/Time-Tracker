from django.urls import path
from . import views

app_name="timedashboard"
urlpatterns = [
    path('', views.AllTimings.as_view(), name='timing'),
    path('/signup', views.Signup.as_view(), name='signup'),
]