from django.db import models


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    amount_type = models.CharField(max_length=255, default='Percentage')

    class Meta:
        verbose_name_plural = "Coupons"
        