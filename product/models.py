from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class GenericName(models.Model):
    category = models.ForeignKey(Category, related_name="generic_category", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=250)
    generic = models.ForeignKey(GenericName, related_name="brand_generic", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, related_name="product_brand", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    no_of_pieces = models.IntegerField(default=3)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='images/product/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    manuf_date = models.DateField()
    expiry_date = models.DateField()


    class Meta:
        ordering = ('-date_added',)


    def __str__(self):
        return self.name


    def get_image(self):
        try:
            return self.image.url
        except:
            return 'media/products/default.jpg'


class Attachments(models.Model):
    uploaded_by = models.ForeignKey(
        User, related_name="attachment_uploaded_by", on_delete=models.SET_NULL, null=True
    )
    file_name = models.CharField(max_length=120)
    uploaded_on = models.DateTimeField(_("Uploaded On"), auto_now_add=True)
    attachment = models.FileField(
        max_length=1001, upload_to="attachments/%Y/%m/")

    def __str__(self):
        return self.uploaded_by.email