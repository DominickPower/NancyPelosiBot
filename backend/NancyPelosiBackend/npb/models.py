from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField
    isActive = models.BooleanField
    createdAt = models.DateField
    expirationDate = models.DateField
    options = models.JSONField(default=dict)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=40)
    createdAt = models.DateField
    suspectIndsideTrader = models.BooleanField

    def __str__(self):
        return self.name

class Bet(models.Model):
    amount = models.DecimalField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)