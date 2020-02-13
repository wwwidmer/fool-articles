from django.db import models

class Comment(models.Model):
    created_at = models.DateTimeField(null=False, auto_now_add=True, blank=True)
    username = models.CharField(max_length=255)
    text = models.TextField(null=False)

    article_uuid = models.CharField(max_length=255, null=False)

