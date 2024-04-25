from django.contrib import admin

from .models import Job, Commission


class CommentInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInline]


admin.site.register(Commission, CommissionAdmin)
