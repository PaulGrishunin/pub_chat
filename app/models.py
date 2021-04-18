from django.db import models
from django.utils import timezone


class Message(models.Model):
    # author = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
