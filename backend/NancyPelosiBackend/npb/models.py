from django.db import models
import uuid
# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    title = models.CharField(max_length=120, default="undefined")
    ticker = models.CharField(max_length=20, default='undefined')
    LastUpdated = models.CharField(max_length=40, default='0')
    category = models.CharField(max_length=20, default='undefined')

    def jsonSerialize(self):
        jsonDict = {}

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