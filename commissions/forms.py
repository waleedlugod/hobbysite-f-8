from django import forms

from .models import Commission, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = "__all__"

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []
