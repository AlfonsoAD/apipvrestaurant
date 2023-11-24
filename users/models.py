import shortuuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField
from handlers.user_handler import validate_roles


class User(AbstractUser):
    email = models.EmailField(unique=True)
    number_employee = models.CharField(
        max_length=22, default=shortuuid.uuid)
    roles = ArrayField(
        models.CharField(max_length=20),
        blank=True,
        null=True,
        validators=[validate_roles]
    )
    image = CloudinaryField('image', blank=True, null=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
