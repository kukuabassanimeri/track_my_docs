from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

app_name = 'track_my_docs'

#urls patterns to route to
urlpatterns = [
    #TrackMyDocs user sign up url pattern
    path('register/', views.user_signup, name='user-signup'),
    
    #TrackMyDocs user Login & logout url
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='user-logout'),
 
    
    #TrackMyDocs user complaint url
    path('complaint/', views.Complaint, name='user-complaint'),
    
    #TrackMyDocs user profile url
    path('profile/', views.userprofile, name='user-profile'),
    
    #TrackMyDocs user password reset url
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='track_my_docs/password_reset.html'), name='password_reset'),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='track_my_docs/password_reset_done.html'), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='track_my_docs/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='track_my_docs/password_reset_complete.html'), name='password_reset_complete'),
    
    #TrackMyDocs Home page url
    path('home/', views.home, name='home'),
    
    #TrackMyDocs user new ID application url
    path('new-id-application/', views.new_id_application, name='new-id-application'),
    
    #TrackMyDocs user ID status correction url
    path('id-status-correction/', views.id_status_correction, name='id-status-correction'),
    
    #TrackMyDocs user lost ID reapplication url 
    path('lost-id-reapplication/', views.lost_id_reapplication, name='lost-id-reapplication'),
]