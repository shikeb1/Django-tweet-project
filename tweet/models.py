from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):

    # Which user created the tweet
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Tweet text content
    text = models.TextField(
        max_length=240
    )

    # Optional photo upload
    photo = models.ImageField(
        upload_to='photos/',
        blank=True,
        null=True
    )

    # Automatically stores creation time
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Automatically updates when edited
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"