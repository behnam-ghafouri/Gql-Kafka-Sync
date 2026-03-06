from django.db import models
from .kafka_utils import emit_deal_created

class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company_id = models.IntegerField()  # References Company in Identity Service

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Deal(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='New')
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='deals')
    company_id = models.IntegerField()

    def save(self,*args,**kwargs):
        is_new = self.pk is None
        super().save(*args,**kwargs)
        if is_new:
            emit_deal_created(self.pk, self.name, self.value)

    def __str__(self):
        return self.name