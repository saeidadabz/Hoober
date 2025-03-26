from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
from .permissions import IsEmployerOrReadOnly, IsApplicantOrReadOnly,IsEmployerOfJob

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsApplicantOrReadOnly]

    def get_permissions(self):
        if self.action in ['update_status']:
            return [IsEmployerOfJob()]
        return [IsAuthenticatedOrReadOnly(),IsApplicantOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


   

    @action(detail=True, methods=['patch'], permission_classes=[IsEmployerOfJob])
    def update_status(self, request, pk=None):
        """
        تغییر وضعیت درخواست شغلی توسط کارفرما
        """
        job_application = self.get_object()
        new_status = request.data.get('status')

        if new_status not in ['accepted', 'rejected']:
            return Response({'error': 'وضعیت نامعتبر است'}, status=status.HTTP_400_BAD_REQUEST)

        job_application.status = new_status
        job_application.save()

        return Response({'message': f'درخواست شغلی {new_status} شد'}, status=status.HTTP_200_OK)
