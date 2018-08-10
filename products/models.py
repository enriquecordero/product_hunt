from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
        title = models.CharField(max_length=200)
        pub_date = models.DateTimeField()
        url = models.TextField(max_length=200)
        body = models.TextField(max_length=200)
        icon = models.ImageField(upload_to='images/')
        image = models.ImageField(upload_to='images/')
        votes_total = models.IntegerField(default=1)
        hunter = models.ForeignKey(User,on_delete=models.CASCADE)

        def __str__(self):
            return self.title

        def summary(self):
            return self.body[:1000]  # dame los primeros 1000 lineas

        def pub_date_pretty(self):
            return self.pub_date.strftime('%b %e %Y')  # para poner la fecha como quiero
