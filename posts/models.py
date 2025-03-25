from django.db import models

# Create your models here.
from users.models import User

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('educational', 'Educational'),  # پست‌های آموزشی
        ('consulting', 'Consulting'),  # پست‌های مشاوره‌ای
        ('job_offer', 'Job Offer'),  # فرصت‌های شغلی (ویژه‌ی کارفرمایان)
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # نوع پست
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author.username}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'