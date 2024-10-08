from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#TrackMyDocs user complaint model
class UserComplaintForm(models.Model):
    name = models.CharField(max_length=100)
    individual_no = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
#TrackMyDocs user profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

#TracKMyDocus user new ID application
class NewIDApplicationModelForm(models.Model):
    name = models.CharField(max_length=100)
    manifest = models.ImageField(default='default.jpg', upload_to='profile_pics')
    headshot = models.ImageField(default='default.jpg', upload_to='profile_pics')
    fingerprint = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.name
    
#TrackMyDocs users ID status correction
class StatusCorrectionModelForm(models.Model):
    user_name = models.CharField(max_length=50)
    user_id = models.ImageField(default='default.jpg', upload_to='profile_pics')
    reason = models.TextField()
        
    def __str__(self):
        return self.user_name

#TrackMyDocs user lost id reapplication

class LostIDReapplicationModelForm(models.Model):
    username = models.CharField(max_length=50)
    police_abstract = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.username
    