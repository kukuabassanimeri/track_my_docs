from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import UserComplaintForm, UpdateUserModelForm, UpdateProfileModelForm
from django.contrib.auth.decorators import login_required
from .forms import NewIDApplicationModelForm, StatusCorrectionModelForm, LostIDReapplicationModelForm, FingerPrintModelForm, RenewIDModelForm
from django.contrib import messages



#TrackMyDocs user signup view
def user_signup(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return redirect('login')
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
            request.session['message'] = "Your complaint is received and it is being reviewed"
            
            return redirect(request.path)
    else:
        context_variable['complaint_form'] = UserComplaintForm()
    return render(request, 'track_my_docs/complaint.html', context_variable)

#TrackMyDocs user profile view
@login_required
def userprofile(request):
    if request.method == "POST":
        u_form = UpdateUserModelForm(request.POST, instance=request.user)
        p_form = UpdateProfileModelForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('track_my_docs:user-profile')
    else:
        u_form = UpdateUserModelForm(instance=request.user)
        p_form = UpdateProfileModelForm(instance=request.user.userprofile)
    context_variable = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'track_my_docs/profile.html', context_variable)

#TrackMyDocs homepage view
@login_required
def home(request):
    return render(request, 'track_my_docs/home.html')

#TrackMyDocs User new Id application view
def new_id_application(request):
    if request.method == 'POST':
        form = NewIDApplicationModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been received and it is being processed.')
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
            messages.success(request, 'Your re-application is received and it is under review')
            return redirect('track_my_docs:lost-id-reapplication')
    else:
        lost_form = LostIDReapplicationModelForm()
    context = {'lost_form': lost_form}
    return render(request, 'track_my_docs/lost_id_reapplication.html', context)

#TrackMyDocs user fingerprint booking view
def fingerprint_booking(request):
    if request.method == 'POST':
        f_form = FingerPrintModelForm(request.POST)
        if f_form.is_valid():
            f_form.save()
            messages.success(request, 'Your fingerprint booking is received and it is under review')
            return redirect('track_my_docs:fingerprint-booking')
    else:
        f_form = FingerPrintModelForm()
    context_v = {'f_form': f_form}
    return render(request, 'track_my_docs/fingerprint_booking.html', context_v)

#TrackMyDocs user renew ID view

def renew_id(request):
    if request.method == 'POST':
        r_form = RenewIDModelForm(request.POST, request.FILES)
        if r_form.is_valid():
            r_form.save()
            messages.success(request, 'Your renewal request is received and it is under review')
            return redirect('track_my_docs:renew-id')
    else:
        r_form = RenewIDModelForm()
    return render(request, 'track_my_docs/renew_id.html', {'r_form': r_form})