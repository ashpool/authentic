import django
from django.db import models, signals
from django.contrib.auth.models import User


class UserLogin(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()

def user_presave(sender, instance, **kwargs):
    if instance.pk and instance.last_login:
        old = instance.__class__.objects.get(pk=instance.pk)
        if instance.last_login != old.last_login:
            instance.userlogin_set.create(timestamp=instance.last_login, user=sender)

#django.db.models.signals.post_save.connect(user_postsave, sender=User)
django.db.models.signals.pre_save.connect(user_presave, sender=User)
