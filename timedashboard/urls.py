from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView


app_name="timedashboard"

urlpatterns = [
    path('', views.AllTimings.as_view(), name='listtiming'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('createtime/', views.CreateTiming.as_view(), name='createtime'),
    path('endtask/<int:pk>/', views.EndTask.as_view(), name='endtask'),
    path('login/', LoginView.as_view(template_name="timedashboard/login.html", redirect_field_name="/createtime"), name='login'),
    path('logout/', LogoutView.as_view(next_page="/signup"), name= 'logout'),
]