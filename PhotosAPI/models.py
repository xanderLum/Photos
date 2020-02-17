from django.db import models
from datetime import datetime


# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.user + ' - ' + self.password


class Photo(models.Model):
    status = models.CharField(max_length=1, default='P')
    caption = models.CharField(max_length=500)
    pubDate = models.DateTimeField(max_length=11, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imageFile = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return str(self.pk) + ' - ' + self.caption + ' - ' + self.status + ' - ' + self.user.user + ' - ' + str(self.pubDate.strftime("%Y-%m-%d %H:%M:%S"))
