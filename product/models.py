from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    pubDate = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votesTotal = models.IntegerField(default=1)
    hunter =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pubDatePretty(self):
        return self.pubDate.strftimr('%b %e %Y')
