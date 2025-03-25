from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet,CommentViewSet,PostCommentsListView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', PostCommentsListView.as_view(), name='post-comments'),  # 📌 مسیر جدید
]