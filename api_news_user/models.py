from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class News(models.Model):
    news_date = models.DateTimeField()
    news_title = models.CharField(max_length=150, verbose_name="title")
    news_text = models.TextField(verbose_name="text")

    def __str__(self):
        return self.news_title

