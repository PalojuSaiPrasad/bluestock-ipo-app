from django.db import models


class IPO(models.Model):
    company_name = models.CharField(max_length=100)
    price_band = models.CharField(max_length=50)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.DecimalField(max_digits=10, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return f"{self.company_name}"  # Create your models here.
