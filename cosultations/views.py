from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import ConsultationSession
from .serializers import ConsultationSessionSerializer
from .permissions import IsConsultant, IsConsultantOwner, CanReserveSession

# Create your views here.

class ConsultationSessionViewSet(viewsets.ModelViewSet):
    """
    ویوست برای مدیریت جلسات مشاوره (CRUD کامل)
    """
    queryset = ConsultationSession.objects.all()
    serializer_class = ConsultationSessionSerializer

    def perform_create(self, serializer):
        serializer.save(consultant=self.request.user)  # مشاور به عنوان مالک جلسه ذخیره می‌شود


    def get_permissions(self):
        """
        تعیین پرمیشن‌ها بسته به نوع درخواست.
        """
        if self.action == "create":
            return [IsConsultant()]  # فقط مشاوران می‌توانند جلسه ایجاد کنند
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsConsultantOwner()]  # فقط مشاور مالک می‌تواند جلسه خود را تغییر دهد یا حذف کند
        elif self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]  # همه کاربران می‌توانند لیست جلسات را ببینند
        return [CanReserveSession()]  # سایر درخواست‌ها (مثلاً رزرو) توسط کاربران ثبت‌نام‌شده انجام شود
    

    @action(detail=True, methods=["patch"], permission_classes=[CanReserveSession])
    def reserve(self, request, pk=None):
        """
        رزرو جلسه مشاوره توسط کاربران عادی
        """
        session = self.get_object()
        if session.client is not None:
            return Response({"error": "این جلسه قبلاً رزرو شده است."}, status=status.HTTP_400_BAD_REQUEST)
        
        session.client = request.user
        session.status = "confirmed"
        session.save()
        return Response({"detail": "جلسه با موفقیت رزرو شد!"})