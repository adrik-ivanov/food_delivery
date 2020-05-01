from django.db import models

# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=256, null=True)
    avatar = models.URLField(max_length=1024, null=False, default='')

    def __str__(self):
        return self.name
