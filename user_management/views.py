from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm


@login_required
def profile_index(request):
    user = request.user
    ctx = {"user": user, "update_link": reverse("user_management:update")}
    return render(request, "registration/profile.html", ctx)


@login_required
def profile_update(request):
    form = ProfileForm()
    ctx = {"form": form}
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.email = form.cleaned_data.get("email")
            user.username = form.cleaned_data.get("username")
            user.password = form.cleaned_data.get("password")
            user.save()
            return redirect("registration/profile-index")

    return render(request, "registration/profile_update.html", ctx)


def register_view(request):
    form = ProfileForm()
    message = ""
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get("first_name")
            lname = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = fname
            new_user.last_name = lname
            new_user.save()
            message = f"{username} has been successully created"

    ctx = {"form": form, "message": message}
    return render(request, "registration/register.html", ctx)
