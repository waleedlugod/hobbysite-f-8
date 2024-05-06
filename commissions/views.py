from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import redirect, render

from commissions.models import Commission, Job, JobApplication

from .forms import CommissionForm, JobApplicationForm


def commission_list(request):
    commission_list = {
        "commission_list": Commission.objects.all(),
        "created_commission_list": Commission.objects.filter(
            author__username=request.user.profile.username
        ),
        "applied_commission_list": Commission.objects.filter(
            job__job_application__applicant__username=request.user.profile.username
        ),
    }
    return render(request, "commission/commission_list.html", commission_list)


@login_required
def commission_detail(request, pk):
    commission_detail = Commission.objects.get(pk=pk)
    commission_jobs = commission_detail.job
    total_manpower_required = commission_jobs.aggregate(Sum("manpower_required"))[
        "manpower_required__sum"
    ] or 0
    open_manpower = (
        total_manpower_required
        - commission_jobs.filter(job_application__status="1").aggregate(
            Count("job_application")
        )["job_application__count"]
    )

    form = JobApplicationForm()
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = Job.objects.get(role=request.POST.get("job"))
            application.applicant = request.user.profile
            application.status = JobApplication.PENDING
            form.save()
            return redirect("commissions:commission_detail", pk=pk)

    commission_detail = {
        "commission_detail": commission_detail,
        "commission_jobs": commission_jobs.all(),
        "total_manpower_required": total_manpower_required,
        "open_manpower": open_manpower,
        "form": form,
    }
    return render(request, "commission/commission_detail.html", commission_detail)


@login_required
def commission_create(request):
    form = CommissionForm()
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("commissions:commission_list")
    ctx = {"form": form}
    return render(request, "commission/commission_create.html", ctx)
