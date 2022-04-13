from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD


class CustomUser(AbstractUser):
    def __str__(self):
        return self.get_full_name()
=======
from django.db import models


class CustomUser(AbstractUser):
    objects = models.Manager()

    def __str__(self):
        return self.get_full_name()

    def __unicode__(self):
        return self.get_full_name()
>>>>>>> github/main
