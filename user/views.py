from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms import UserLoginForm, ProfileForm, UserRegisterForm
from django.contrib import messages

from user.models import Profile


def user_register(request):
    user_form = UserRegisterForm()
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data.get("email")
            user.save()
            return redirect("list_task")
    context = {"form": user_form}

    return render(request, "user/home.html", context)


def user_login(request):
    user_login_form = UserLoginForm()
    if request.method == "POST":
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"User {username} was login successfully")
                return redirect('home')
            messages.error(request, "failed to log in")
    context = {"form": user_login_form}

    return render(request, "user/user_login.html", context)


def user_logout(request):
    logout(request)
    return redirect("user_login")


@login_required(login_url="user_login")
def user_profile(request, user_id):
    try:
        profile = Profile.objects.get(user_id=user_id)
    except Profile.DoesNotExist:
        messages.info(request, "you don't have Profikle yet")
        return redirect('list_task')

    return render(request, "user/profile.html", context={"profile": profile})


@login_required(login_url="user_login")
def profile_update(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id, user_id=request.user.id)
    except Profile.DoesNotExist:
        return redirect("home")
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)

            if request.FILES.get('image', None) != None:
                profile.image = request.FILES['image']
                profile.save()
            return redirect("user_profile", user_id=request.user.id)

    return render(request, "user/profile_update.html", {'form': form})
