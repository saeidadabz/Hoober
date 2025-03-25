from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import PostPermission
from drf_spectacular.utils import extend_schema

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [PostPermission]  # استفاده از مجوزها برای اعتبارسنجی

    @extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer},
    )

    def perform_create(self, serializer):
        """ تعیین نویسنده‌ی پست هنگام ایجاد آن """
        serializer.save(author=self.request.user)