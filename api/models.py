from django.db import models


class TrustedToken(models.Model):
    token = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
