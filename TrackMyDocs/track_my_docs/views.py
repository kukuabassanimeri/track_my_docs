from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import UserComplaintForm
from django.contrib.auth.decorators import login_required
from .forms import NewIDApplicationModelForm, StatusCorrectionModelForm, LostIDReapplicationModelForm
from django.contrib import messages


#TrackMyDocs user signup view
def user_signup(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return redirect('track_my_docs:user-login')
    else:
        user_form = UserRegisterForm()
    return render(request, 'track_my_docs/register.html', {'form': user_form})

#TrackMyDocs user complaint view
def Complaint(request):
    
    context_variable = {}
    
    #create session
    if request.session.get('message', None):
        message = request.session.get('message')
        context_variable['message'] = message
        del request.session['message']
    
    if request.method == "POST":
        complaint_form = UserComplaintForm(request.POST)
        if complaint_form.is_valid():
            complaint_form.save()
            request.session['message'] = "Your request has been received, we will get back to you soon"
            
            return redirect(request.path)
    else:
        context_variable['complaint_form'] = UserComplaintForm()
    return render(request, 'track_my_docs/complaint.html', context_variable)

#TrackMyDocs user profile view
def userprofile(request):
    return render(request, 'track_my_docs/profile.html')

#TrackMyDocs homepage view

def home(request):
    return render(request, 'track_my_docs/home.html')

#TrackMyDocs User new Id application view
def new_id_application(request):
    if request.method == 'POST':
        form = NewIDApplicationModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been received. We will get back to you shortly.')
            return redirect('track_my_docs:new-id-application')
    else:
        form = NewIDApplicationModelForm()

    context = {'form': form}
    return render(request, 'track_my_docs/new_id_application_form.html', context)

#TrackMyDocs user Id status correction view
def id_status_correction(request):
    if request.method == 'POST':
        form = StatusCorrectionModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your correction request has been received. And it is under review.')
            return redirect('track_my_docs:id-status-correction')
    else:
        form = StatusCorrectionModelForm()
    context = {'form': form}
    return render(request, 'track_my_docs/id_status_correction.html', context)

# TrackMyDocs user lost Id reapplication view
def lost_id_reapplication(request):
    if request.method == 'POST':
        lost_form = LostIDReapplicationModelForm(request.POST, request.FILES)
        if lost_form.is_valid():
            lost_form.save()
            messages.success(request, 'Your reapplication was successful. It is now under review')
            return redirect('track_my_docs:lost-id-reapplication')
    else:
        lost_form = LostIDReapplicationModelForm()
    context = {'lost_form': lost_form}
    return render(request, 'track_my_docs/lost_id_reapplication.html', context)