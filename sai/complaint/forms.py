from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Complaints,Poll

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(
        attrs= {
        'class':'form-control',
        'placeholder':'Email Id'
        }
    ))
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Enter Username..."
        }
    ))
    first_name = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Enter First Name...."
        }
    ))
    last_name = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Enter Last Name....."
        }
    ))
    password1 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Enter password...."
        }
    ))
    password2 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Re-enter password...."
        }
    ))
    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )
    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return user



class Complaintform(forms.ModelForm):
    CHOICES = (
            ('cse','CSE-dept'),
            ('it','It-dept'),
            ('ece','ECE-dept'),
    		('eee','EEE-dept'),
    		('mech','MECH-dept'),
    		('exam','Examination-branch'),
    		('maintenance','MAINTENANCE'),
        )
    complaintno = forms.IntegerField(widget = forms.TextInput(
        attrs= {
        'class':'form-control',
        'placeholder':'enter complaint no'
        }
    ))
    title = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Enter your title..."
        }
    ))
    description  = forms.CharField(widget = forms.Textarea(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Complaints..."
        }
    ))


    class Meta:
    	model = Complaints
    	fields=(
            'complaintno',
    		'title',
    		'description',
            'category',
    		)

# class PollForm(forms.ModelForm):
#         class Meta:
#             model = Poll
#             fields = (
#                 'lecturer1',
#                 'lecturer2',
#                 'lecturer3',
#                 )

# class ChoiceForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = ('choice',)
