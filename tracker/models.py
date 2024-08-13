from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()
    expense_type = models.CharField(choices=(('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')),max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



class RequestLogs(models.Model):
    request_info = models.TextField()
    request_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
