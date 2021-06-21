from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.

class Category(models.Model):
    category = models.CharField(primary_key = True, max_length=256)

    def __str__(self):
        return self.category

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    start_price = models.IntegerField()
    now_price = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    end_date = models.DateTimeField(default = datetime.now(timezone.utc) + timedelta(days=3))
    remaining_time = models.DateTimeField(blank=True, null = True)
    buyer = models.CharField(max_length=20, blank=True, null=True)

    def bidding(self):
        self.now_price += 100
        self.save()

    def __str__(self):
        return self.title
