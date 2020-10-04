from django import forms
from django.contrib.auth.models import User
from .models import Timing, Project


class SignupForm(forms.ModelForm):
	"""
		override the password field to get a change input type of password.
		add verify_password field to verify to user's password.
	"""
	password = forms.CharField(widget=forms.PasswordInput,label="Password")
	verify_password = forms.CharField(widget=forms.PasswordInput,label="Password (again)")
	
	class Meta:
		model=User
		fields=['username', 'first_name', 'last_name', 'email','password']

	def clean(self):
		# override clean function to verify extra conditions(verify  password).
		cleaned_data = super(SignupForm, self).clean()
		if 'password' in self.cleaned_data and 'verify_password' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['verify_password']: # password and verify_password field should be the same
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
			else:
				del cleaned_data['verify_password'] # non-useful field removed.
				return self.cleaned_data
	
	def save(self, commit=True):
		user = super(SignupForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password']) # set password in user instance
		if commit is True:
			user.save()
		return user


class CreateTimingForm(forms.ModelForm):
	class Meta:
		model=Timing
		fields= ['project', 'task']

	def __init__(self, *args,**kwargs):
		super().__init__(*args, **kwargs)
		# get all projects from Project table
		self.fields['project'].queryset = Project.objects.all()
