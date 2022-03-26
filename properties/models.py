from django.db import models
import datetime
from django.conf import settings

def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]


class Property(models.Model):

    YEARS=year_choices()
    PROPERTY_PLANIMETRIES = [
        ('GS','Garsonier'),
        ('1_1','1+1'),
        ('2_1', '2+1'),
        ('3_1', '3+1'),
        ('DP', 'Duplex'),
        ('VL', 'Villa'),
        ('MS', 'Mansion'),
        ('GR', 'Garage')
    ]
    address = models.TextField(verbose_name='Address of the property!',null=False, blank=False)
    planimetry = models.CharField(verbose_name='Planimetry of the property!', max_length=3,choices=PROPERTY_PLANIMETRIES,null=False,default='1_1')
    size = models.FloatField(verbose_name='Size in squared meters.')

    #add constraint for greater than 0
    #add cunrrency conversion

    price = models.FloatField(verbose_name='Price in euros',null=False,blank=False)
    description = models.TextField(verbose_name='Description for the house',null=True,blank=True)
    city = models.ForeignKey(to='City',on_delete=models.PROTECT,null=False, blank=False)
    built_year = models.IntegerField(verbose_name='Built year',choices=YEARS,null=False,default=datetime.date.today().year)
    floor = models.IntegerField(verbose_name="Property floor",null=True,blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False,blank=False)



class City(models.Model):
    name=models.CharField(max_length=15,unique=True, null=False,blank=False)

