from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



class Province(models.Model):
    country = models.ForeignKey(Country, related_name="province_country" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class District(models.Model):
    country = models.ForeignKey(Country, related_name="district_country", on_delete=models.CASCADE)
    province = models.ForeignKey(Province, related_name="district_province" , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


# class City(models.Model):
#     country = models.ForeignKey(Country, related_name="city_country", on_delete=models.CASCADE)
#     province = models.ForeignKey(Province, related_name="city_province" , on_delete=models.CASCADE)
#     district = models.ForeignKey(Province, related_name="city_district" , on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)


#     class Meta:
#         ordering = ('name',)

    
#     def __str__(self):
#         return self.name

