from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    # se añaden los campos adicionales a los que estan en el modelo AbstractUser
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
