from django.db import models
from django.contrib.auth.models import User

class payments(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)
    order_id=models.CharField(max_length=50)
    isPaid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.amount
    