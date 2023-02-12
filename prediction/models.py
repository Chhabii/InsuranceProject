from django.db import models

# Create your models here.
class Insurance(models.Model):
    GENDER = (
        ("Male","Male"),
        ("Female","Female")
    )
    DRIVING_LICENSE = (
        (1,"YES"),
        (0,"NO")
    )
    PREVIOUSLY_INSURED = (
        (1,"YES"),
        (0,"NO")
    )
    VEHICLE_AGE = (
        ("> 2 Years","> 2 Years"),
        ("1-2 Year","1-2 Year"),
        ("< 1 Year","< 1 Year")
    )
    VEHICLE_DAMAGE =(
        ("Yes","YES"),
        ("No","NO")
    )
    id = models.AutoField(primary_key=True)
    Gender = models.CharField(max_length=6,choices=GENDER,null=True)
    Age = models.IntegerField(null=True)
    Driving_License = models.IntegerField(choices=DRIVING_LICENSE,null=True)
    Region_Code = models.IntegerField(null=True)
    Previously_Insured = models.IntegerField(choices=PREVIOUSLY_INSURED,null=True)
    Vehicle_Age = models.CharField(max_length=15,choices=VEHICLE_AGE,null=True)
    Vehicle_Damage = models.CharField(max_length=3,choices=VEHICLE_DAMAGE,null=True)
    Annual_Premium = models.FloatField(null=True)
    Policy_Sales_Channel = models.FloatField(null=True)
    Vintage = models.IntegerField(null=True)