from django.db import models
from django.contrib.auth.models import User


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Topic(TimeStampedMixin):
    text = models.CharField(max_length=124)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(TimeStampedMixin):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.text[:50] + "...."
