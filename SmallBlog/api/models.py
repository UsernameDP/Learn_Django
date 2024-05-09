from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    username = models.CharField(max_length=250)

    def __str__(self):
        return self.title
