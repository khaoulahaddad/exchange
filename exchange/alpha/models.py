from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    from_currency = models.CharField(max_length=256, blank=True, null=True)
    to_currency =models.CharField(max_length=256, blank=True, null=True)
    value =models.FloatField()
    last_refresh = models.DateTimeField()
    def __str__(self):
        return self.name

