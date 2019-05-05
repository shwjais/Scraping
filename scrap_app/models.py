from django.db import models

class headlines(models.Model):
    top_name = models.CharField(max_length=400)

    def __str__(self):
        return self.top_name


# Create your models here.

