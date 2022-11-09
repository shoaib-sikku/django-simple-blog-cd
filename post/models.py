from email.policy import default
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    description = models.TextField()

