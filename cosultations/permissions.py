from rest_framework import permissions

class IsConsultant(permissions.BasePermission):
    """
    فقط مشاوران (consultant) می‌توانند جلسات ایجاد کنند.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "consultant"


class IsConsultantOwner(permissions.BasePermission):
    """
    فقط مشاوری که جلسه را ایجاد کرده، می‌تواند آن را ویرایش یا حذف کند.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.consultant == request.user


class CanReserveSession(permissions.BasePermission):
    """
    فقط کاربران عادی (نه مشاوران) می‌توانند جلسه رزرو کنند، اگر هنوز رزرو نشده باشد.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role == "normal" and obj.client is None