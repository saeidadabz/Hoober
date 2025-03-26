from rest_framework import serializers
from .models import ConsultationSession

class ConsultationSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ConsultationSession
        fields = "__all__"
        read_only_fields = ["consultant", "created_at"]