from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Publish'))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # auto_now_add=True this will generate the current date and time and save it to the post table
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    # on_delete=models.CASCADE means if the user is deleted from the database, every post of the user will also be
    # deleted.
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    # this will allow the name of the object be displayed in the admin page -
    # (will return string representation of the object).
    def __str__(self):
        return self.title
