from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Profile
from .forms import RegisterForm


def register_view(request):
    form = RegisterForm()
    message = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
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
