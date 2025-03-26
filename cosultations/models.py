from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class ConsultationSession(models.Model):
    consultant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consultations")  # مشاور
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="appointments")  # مراجعه‌کننده
    title = models.CharField(max_length=255)  # عنوان جلسه
    description = models.TextField(blank=True)  # توضیحات
    start_time = models.DateTimeField()  # زمان شروع
    end_time = models.DateTimeField()  # زمان پایان
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("canceled", "Canceled"),
            ("completed", "Completed"),
        ],
        default="pending",
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.consultant}"