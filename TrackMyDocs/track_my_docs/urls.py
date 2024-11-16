from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

app_name = 'track_my_docs'

#urls patterns to route to
urlpatterns = [
    #TrackMyDocs user sign up url pattern
    path('register/', views.user_signup, name='user-signup'),
    
    #TrackMyDocs user complaint url
    path('complaint/', views.Complaint, name='user-complaint'),
    
    #TrackMyDocs user profile url
    path('profile/', views.userprofile, name='user-profile'),
    
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
      
    #TrackMyDocs Home page url
    path('home/', views.home, name='home'),
    
    #TrackMyDocs user new ID application url
    path('new-id-application/', views.new_id_application, name='new-id-application'),
    
    #TrackMyDocs user ID status correction url
    path('id-status-correction/', views.id_status_correction, name='id-status-correction'),
    
    #TrackMyDocs user lost ID reapplication url 
    path('lost-id-reapplication/', views.lost_id_reapplication, name='lost-id-reapplication'),
    
    #TrackMyDocs user fingerprint booking
    path('fingerprint_booking/', views.fingerprint_booking, name='fingerprint-booking'),
    
    #TrackMyDocs user renew expired id
    path('renew-id/', views.renew_id, name='renew-id')
]