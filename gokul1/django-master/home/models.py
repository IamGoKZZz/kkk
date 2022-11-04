from django.db import models


# Create your models here.
class EgModel(models.Model):
    string_field = models.CharField(max_length=100)
    textarea = models.TextField()
    integer = models.IntegerField()
    floating_number = models.FloatField()
    date_filed = models.DateField()
    image_filed = models.ImageField(upload_to="images")
class Blog(models.Model):
    blognumber=models.IntegerField(default=1)
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to="images")
    date= models.DateField()
    def __str__(self):
        return self.title
    price=models.FloatField()
    Watchnow=models.VideoCapture()
