from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, FormView, DetailView
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import SignupForm, CreateTimingForm
from .models import Timing, Project
import datetime


class CreateTiming(CreateView, LoginRequiredMixin):
	template_name="timedashboard/createtime.html"
	login_url = '/signup/'
	form_class= CreateTimingForm
	success_url = reverse_lazy('timedashboard:listtiming')

	def form_valid(self, form):
		new_work = form.save(commit=False)
		new_work.user = self.request.user
		new_work.save()
		return HttpResponseRedirect(self.success_url)


class AllTimings(LoginRequiredMixin, ListView):
	template_name="timedashboard/timing_list.html"
	allow_empty= True
	login_url = '/signup/'
	def get_queryset(self):
		return Timing.objects.filter(user=self.request.user).order_by("start").reverse()


class EndTask(DetailView):
	def get(self, request, pk):
		curr_task=Timing.objects.filter(pk=pk).first()
		curr_task.end=datetime.datetime.now()
		curr_task.save()
		return redirect(reverse('timedashboard:listtiming',))


class Signup(CreateView):
	form_class= SignupForm
	template_name= "timedashboard/signup.html"
	success_url = reverse_lazy('timedashboard:listtiming')
	
	def form_valid(self, form):
		valid = super(Signup, self).form_valid(form)
		username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
		new_user = authenticate(username=username, password=password)
		login(self.request, new_user)
		return valid