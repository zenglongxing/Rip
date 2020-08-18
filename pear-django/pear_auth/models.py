from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    salt = models.CharField(verbose_name="盐值", max_length=100, null=False)

    class Meta:
        verbose_name = "用户关联表"

    def __str__(self):
        return self.user.__str__()
