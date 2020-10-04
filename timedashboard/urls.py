from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView


app_name = 'timedashboard'

urlpatterns = [
    path('', views.AllTimings.as_view(), name = 'listtiming'),
    path('signup/', views.Signup.as_view(), name = 'signup'),
    path('createtime/', views.CreateTiming.as_view(), name = 'createtime'),
    path('endtime/<int:pk>/', views.EndTask.as_view(), name = 'endtask'),
    path('login/', LoginView.as_view(template_name = 'timedashboard/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]
