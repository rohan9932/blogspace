from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_author"
    )

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Content', config_name='extends')
    view_count = models.PositiveBigIntegerField(default=0)
    liked_users = models.ManyToManyField(User, related_name='liked_users')

    def __str__(self) -> str:
        return self.title


class Comment(BaseModel):
    content = models.TextField()
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='post_comments'
    )

    def __str__(self) -> str:
        return f"Comment by {self.author.username}"
