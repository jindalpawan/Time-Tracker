import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, FormView, DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy

from .forms import SignupForm, CreateTimingForm
from .models import Timing, Project


class CreateTiming(LoginRequiredMixin, CreateView):
	"""
		CreateView
			I used CreateView to create a new instance of work/time.
			Createview that provides the functionality to create new objects very easily.

		LoginRequiredMixin
			Used to implement login required functionality in the class and also it allows us to specify a URL for login.
	"""
	template_name = 'timedashboard/createtime.html'
	login_url = '/signup/' # to login
	form_class = CreateTimingForm
	allow_empty = True
	success_url = reverse_lazy('timedashboard:listtiming')  # go to this URL after creating new object/work

	def form_valid(self, form):
		new_work = form.save(commit = False)
		new_work.user = self.request.user
		new_work.save()
		return HttpResponseRedirect(self.success_url)


class AllTimings(LoginRequiredMixin, ListView):
	"""
		ListView
			I used ListView to print/show all the previous timings.
			ListView provides a list- object_list which has queryset data.

		LoginRequiredMixin
			Used to implement login required(user must be login) functionality in the class and also it allows us to specify a URL for login.
	"""
	template_name = 'timedashboard/timing_list.html'
	allow_empty = True
	login_url = '/signup/'

	def get_queryset(self):
		# all the previous timings.
		return Timing.objects.filter(user = self.request.user).select_related('project').order_by("start").reverse()


class EndTask(DetailView):
	
	def get(self, request, pk):
		# end current timing.
		curr_task = Timing.objects.filter(pk = pk).first()
		curr_task.end = datetime.datetime.now()
		curr_task.save(update_fields = ['end'])
		return redirect(reverse('timedashboard:listtiming',))


class Signup(CreateView):
	"""
		CreateView
			I used CreateView to create a new user instance and after creating a new user it will go to create a timing instance.
			CareteView provides functionality to create new objects very easily.
	"""
	form_class = SignupForm
	template_name = 'timedashboard/signup.html'
	success_url = reverse_lazy('timedashboard:createtime')
	
	def form_valid(self, form):
		valid = super(Signup, self).form_valid(form)
		username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
		new_user = authenticate(username = username, password = password)
		login(self.request, new_user) # login new user
		return valid
