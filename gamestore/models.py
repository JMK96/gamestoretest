from django.conf import settings
from django.db import models
from django.utils import timezone

class Game(models.Model):
        developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        description = models.TextField()
        published_date = models.DateTimeField(blank=True, null=True)

        def __str__(self):
            return self.title
# Create your models here.
