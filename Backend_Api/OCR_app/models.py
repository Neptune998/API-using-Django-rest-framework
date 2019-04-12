from django.db import models


# Model for user login and signup
class User_model(models.Model):
    email = models.EmailField()
    Name = models.CharField(max_length=20)
    password =models.CharField(max_length=20)
    Confirm =models.CharField(max_length=20)

    def __str__(self):
        return self.Name


