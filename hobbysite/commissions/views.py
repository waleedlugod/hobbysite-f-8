from django.shortcuts import render

from commissions.models import Comment, Commission


def commission_list(request):
    commission_list = {"commission_list": Commission.objects.all()}
    return render(request, "commission_list.html", commission_list)
