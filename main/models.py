from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=254)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.CharField(max_length=20)
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
