from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ProfileForm, RegisterForm
from .models import Profile


@login_required
def profile_dashboard(request):
    user = request.user
    ctx = {"user": user, "update_link": reverse("user_management:update")}
    return render(request, "registration/profile.html", ctx)


@login_required
def profile_update(request):
    form = ProfileForm()
    ctx = {"form": form}
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("user_management:dashboard")

    return render(request, "registration/profile_update.html", ctx)


def register_view(request):
    form = RegisterForm()
    message = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username, email, password)
            new_user.save()

            profile = Profile()
            profile.user = new_user
            profile.username = form.cleaned_data.get("username")
            profile.email = form.cleaned_data.get("email")
            profile.save()

            message = f"{username} has been successully created"

    ctx = {"form": form, "message": message}
    return render(request, "registration/register.html", ctx)
