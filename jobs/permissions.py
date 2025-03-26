from rest_framework import permissions


class IsEmployerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.employer == request.user

class IsApplicantOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.applicant == request.user
    
class IsEmployerOfJob(permissions.BasePermission):
    """
    فقط کارفرمایی که شغل را ایجاد کرده می‌تواند درخواست‌های مربوط به آن را مدیریت کند.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employer'

    def has_object_permission(self, request, view, obj):
        return obj.job.employer == request.user  # فقط کارفرمای این شغل