from django.db import models


class Image(models.Model):
    Name = models.CharField(max_length=50)
    DOB = models.DateField()

    def __str__(self):
        return self.Name




