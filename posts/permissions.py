from rest_framework import permissions

class PostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # بررسی اینکه آیا کاربر وارد شده است یا خیر
        if not request.user.is_authenticated:
            return False

        # برای ایجاد پست نیاز به ورود کاربر است
        if request.method == 'POST':
            category = request.data.get('category')
            user_type = request.user.user_type  # فرض می‌کنیم user_type در مدل User موجود است

            # فقط مشاوران می‌توانند پست‌های مشاوره‌ای بگذارند
            if category == 'consulting' and user_type != 'consultant':
                return False
            
            # فقط کارفرمایان می‌توانند پست‌های فرصت شغلی بگذارند
            if category == 'job_offer' and user_type != 'employer':
                return False

            # همه کاربران می‌توانند پست آموزشی بگذارند
            if category == 'educational':
                return True

            return False

        return True

    def has_object_permission(self, request, view, obj):
        # بررسی اینکه کاربر فقط می‌تواند پست‌های خود را ویرایش یا حذف کند
        if view.action in ['update', 'partial_update', 'destroy']:  # برای ویرایش یا حذف
            return obj.author == request.user  # فقط نویسنده پست می‌تواند آن را ویرایش یا حذف کند
        return True
    

class CommentPermission(permissions.BasePermission):
    """
    - فقط نویسنده‌ی کامنت می‌تواند آن را ویرایش یا حذف کند.
    - کاربران دیگر فقط امکان مشاهده دارند.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  
            return True
        return obj.author == request.user  # فقط نویسنده می‌تواند تغییر دهد.