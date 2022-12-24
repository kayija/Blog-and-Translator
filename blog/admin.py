from django.contrib import admin
# this will import the model
from .models import Post


# this will create more columns in the admin view
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')


# Register your models here.
# this will allow you to add data to the database from the admin page
admin.site.register(Post, PostAdmin)
