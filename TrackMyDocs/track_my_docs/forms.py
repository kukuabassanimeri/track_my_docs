from django import forms
from django.contrib.auth.models import User
from .models import UserComplaintForm, NewIDApplicationModelForm, StatusCorrectionModelForm, LostIDReapplicationModelForm

#TrackMyDocs user registration form
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email']

#TrackMyDocs user login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField( widget=forms.PasswordInput)
    

#TrackMyDocs user contact us form
class UserComplaintForm(forms.ModelForm):
    class Meta:
        model = UserComplaintForm
        fields = '__all__'

#TrackMyDocs user new Id application
class NewIDApplicationModelForm(forms.ModelForm):
    class Meta:
        model = NewIDApplicationModelForm
        fields = ['individual_no', 'name', 'nationality', 'manifest', 'headshot', 'fingerprint' ]

#TrackMyDocs user ID status correction
class StatusCorrectionModelForm(forms.ModelForm):
    class Meta:
        model = StatusCorrectionModelForm
        fields = ['user_name', 'user_id', 'reason']

# TrackMyDocs user lost Id reapplication

class LostIDReapplicationModelForm(forms.ModelForm):
    class Meta:
        model = LostIDReapplicationModelForm
        fields = ['username', 'police_abstract']