from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import redirect, render

from commissions.models import Commission, Job, JobApplication

from .forms import CommissionForm, JobApplicationForm, JobForm


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
    total_manpower_required = (
        commission_jobs.aggregate(Sum("manpower_required"))["manpower_required__sum"]
        or 0
    )
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
    commission_form = CommissionForm()
    job_form = JobForm()
    if request.method == "POST":
        commission_form = CommissionForm(request.POST)
        job_form = JobForm(request.POST)
        if commission_form.is_valid() and job_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission = commission_form.save()
            job = job_form.save(commit=False)
            job.commission = commission
            job_form.save()
            return redirect("commissions:commission_list")
    ctx = {"commission_form": commission_form, "job_form": job_form}
    return render(request, "commission/commission_create.html", ctx)


@login_required
def commission_edit(request, pk):
    commission_form = CommissionForm()
    if request.method == "POST":
        commission = Commission.objects.get(pk=pk)
        commission_form = CommissionForm(request.POST, instance=commission)
        if commission_form.is_valid():
            commission_form.save()
    # TODO: make jobs editable
    ctx = {"commission_form": commission_form}
    return render(request, "commission/commission_edit.html", ctx)
