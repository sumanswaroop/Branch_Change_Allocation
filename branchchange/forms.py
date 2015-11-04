from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BranchChangeUsers(UserCreationForm):
	rollno = forms.CharField( max_length = 9 ,min_length = 9, required = True, widget =forms.TextInput(attrs={'placeholder': 'Roll No in 15XXXXXXX' , 'class': 'form-control' }))
	
	class Meta:
		model = User
		fields = {'username', 'rollno', 'password1', 'password2'}
		widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name' , 'class': 'form-control' }),
  
        }
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken. Please select another")

	def save(self, commit = True):
		user = super(BranchChangeUsers , self).save(commit=False)
		user.first_name = self.cleaned_data['rollno']
		if commit:
			user.save()
		return user