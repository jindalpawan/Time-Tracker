from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
import os
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import SignupForm
from .models import Timing, Project

class Signup(CreateView):
	model= User
	template_name= "timedashboard/signup.html"
	fields= ['username', 'email', 'password', 'first_name', 'last_name']
	def get_form(form_class=None):
		return SignupForm

#class Login(TemplateView):


class AllTimings(ListView):
	template_name="timedashboard/timing_list.html"
	allow_empty= True
	queryset= User.objects.filter(pk=request.user.pk).order_by("start").reverse()

#class UpdateEndTime(UpdateView):
