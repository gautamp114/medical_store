from country.models import Country, District, Province
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

SEX = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)

ROLE = (
    ('1','Vendor'),
    ('2','Customer'),
)

class CustomUser(AbstractUser):
    contact_number = PhoneNumberField(
        _("Mobile Number"), unique=True)
    sex = models.CharField(_("Gender"),choices=SEX, max_length=7, default="Male")

    class Meta:
        ordering = ["id",]


