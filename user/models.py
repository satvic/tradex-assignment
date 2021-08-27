from django.db import models
from django.contrib.auth.models import User


# User and Post models with foreign key
class Post(models.Model):
    text = models.TextField(max_length=300)
    author = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} {self.created_at}'
