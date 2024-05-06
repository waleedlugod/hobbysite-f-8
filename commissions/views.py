from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from commissions.models import Commission


def commission_list(request):
    commission_list = {
        "commission_list": Commission.objects.all(),
        "created_commission_list":
        Commission.objects.filter(author__username=request.user.profile.username),
        "applied_commission_list": Commission.objects.filter(
            job__job_application__applicant__username=request.user.profile.username
        ),
    }
    return render(request, "commission/commission_list.html", commission_list)


@login_required
def commission_detail(request, pk):
    commission_detail = {"commission_detail": Commission.objects.get(pk=pk)}
    return render(request, "commission/commission_detail.html", commission_detail)
