from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ProfileForm


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
            return redirect("registration/profile-index")

    return render(request, "registration/profile_update.html", ctx)


def register_view(request):
    form = ProfileForm()
    message = ""
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            message = f"{profile.username} has been successully created"

    ctx = {"form": form, "message": message}
    return render(request, "registration/register.html", ctx)
