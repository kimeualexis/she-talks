from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('girlapp:issue-detail', args=[str(self.pk)])


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
