from django import forms
from django.contrib.auth.models import User
from .models import (UserComplaintForm, NewIDApplicationModelForm, StatusCorrectionModelForm, LostIDReapplicationModelForm, UserProfile, FingerPrintModelForm, RenewIDModelForm)

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
    

#TrackMyDocs user complaint form
class UserComplaintForm(forms.ModelForm):
    class Meta:
        model = UserComplaintForm
        fields = '__all__'

#TrackMyDocs user new Id application
class NewIDApplicationModelForm(forms.ModelForm):
    class Meta:
        model = NewIDApplicationModelForm
        fields = [ 'full_name', 'manifest', 'headshot', 'fingerprint' ]
        
        def clean(self):
            cleaned_data = super().clean()

        # Check that each file field has a file uploaded
            for field in ['manifest', 'headshot', 'fingerprint']:
                if not cleaned_data.get(field):
                    self.add_error(field, f"Please upload a file for {field}.")

            return cleaned_data

#TrackMyDocs user ID status correction
class StatusCorrectionModelForm(forms.ModelForm):
    class Meta:
        model = StatusCorrectionModelForm
        fields = ['full_name', 'id_card', 'reason']

# TrackMyDocs user lost Id reapplication
class LostIDReapplicationModelForm(forms.ModelForm):
    class Meta:
        model = LostIDReapplicationModelForm
        fields = ['full_name', 'police_abstract']

#TrackMyDocs update user form
class UpdateUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
# TrackMyDocs user update profile form
class UpdateProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']
        
#TrackMyDocs user FingerPrint Booking form
class FingerPrintModelForm(forms.ModelForm):
    class Meta:
        model = FingerPrintModelForm
        fields = ['full_name', 'individual_no', 'message']
        
# TrackMyDocs user Renew ID form

class RenewIDModelForm(forms.ModelForm):
    class Meta:
        model = RenewIDModelForm
        fields = ['full_name', 'expired_id']