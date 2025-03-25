from django.shortcuts import render
from rest_framework import viewsets, permissions , generics
from rest_framework.exceptions import NotFound
from .models import Post , Comment
from .serializers import PostSerializer , CommentSerializer
from .permissions import PostPermission , CommentPermission
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



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermission]

    @extend_schema(
    request=CommentSerializer,
    responses={201: PostSerializer},
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostCommentsListView(generics.ListAPIView):
    """
    این ویو فقط کامنت‌های مربوط به یک پست خاص رو برمی‌گردونه
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]  # 👈 می‌تونید این رو تغییر بدید

 
    def get_queryset(self):
        post_id = self.kwargs['post_id']  # 📌 گرفتن post_id از URL
        
        # بررسی اینکه آیا این پست وجود دارد؟
        if not Post.objects.filter(id=post_id).exists():
            raise NotFound(detail="پستی با این شناسه یافت نشد.", code=404)

        return Comment.objects.filter(post_id=post_id).order_by('-created_at')