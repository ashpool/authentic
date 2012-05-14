import django
from django.db import models, signals
from django.contrib.auth.models import User

# Create your models here.

class UserLogin(models.Model):
    """Represent users' logins, one per record"""
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()

def user_presave(sender, instance, **kwargs):
    if instance.last_login:
        old = instance.__class__.objects.get(pk=instance.pk)
        if instance.last_login != old.last_login:
            instance.userlogin_set.create(timestamp=instance.last_login)

django.db.models.signals.pre_save.connect(user_presave, sender=User)
