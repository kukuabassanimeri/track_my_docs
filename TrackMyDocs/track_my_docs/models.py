from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


#TrackMyDocs user complaint model
class UserComplaintForm(models.Model):
    name = models.CharField(max_length=100, blank=False)
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
    
    #override the save method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

#TracKMyDocus user new ID application
class NewIDApplicationModelForm(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    manifest = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=False, null=False)
    headshot = models.ImageField(default='default.jpg', upload_to='profile_pics')
    fingerprint = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.full_name
    
#TrackMyDocs users ID status correction
class StatusCorrectionModelForm(models.Model):
    full_name = models.CharField(max_length=50)
    id_card = models.ImageField(default='default.jpg', upload_to='profile_pics')
    reason = models.TextField()
        
    def __str__(self):
        return self.full_name

#TrackMyDocs user lost id reapplication
class LostIDReapplicationModelForm(models.Model):
    full_name = models.CharField(max_length=50)
    police_abstract = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.full_name
    
#TrackMyDocs user lost FingerPrint Booking
class FingerPrintModelForm(models.Model):
    full_name = models.CharField(max_length=50)
    individual_no = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
#TrackMyDocs user expired Id renewal
class RenewIDModelForm(models.Model):
    full_name = models.CharField(max_length=50)
    expired_id = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.full_name