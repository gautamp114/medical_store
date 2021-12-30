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
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    # dob = models.DateField()
    # address = models.CharField(max_length=50)
    # business_type = models.CharField(max_length=10, choices=ROLE, default="1")

    # USERNAME_FIELD = 'contact_number'

    class Meta:
        ordering = ["id",]

    @property
    def is_admin(self):
        return self.is_superuser
        # return self.business_type == 1 or self.is_superuser


