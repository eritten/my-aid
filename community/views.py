from django.shortcuts import render, redirect
from .forms import UserForm, CreateProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.hashers import make_password

# Create your views here.
def check_profile(u):
    return not(Profile.objects.get(user__username=u.username).create_profile)

@login_required
@user_passes_test(check_profile)
def create_profile(request):
    form = CreateProfile()
    if request.method == "POST":
        form = CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.create_profile = True
            profile.user = request.user;profile.save()
            messages.success(request, "Profile created")
        return render(request, "profile/create_profile.html", {"form": form})
    return render(request, "profile/create_profile.html", {"form": form})

def create_account(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            password = make_password(request.POST.get('password'))
            user = form.save(commit=False)
            user.password = password;user.save()
            messages.success(request, "Account created")
        return render(request, "register/create_form.html", {"form": form})
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, "register/create_form.html", {"form": form})



def login_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.success(request, "Login failed")
        return render(request, "register/login.html")

    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, "register/login.html")

@login_required
def dashboard(request):
    is_activated = Profile.objects.filter(user__username=request.user.username)
    return render(request, 'dashboard/dashboard.html', {'is_activated': is_activated})

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logout.html')
