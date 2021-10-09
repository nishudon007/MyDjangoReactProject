from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    # auto_now_add is a flag that needs to be setup as true
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# str -> string ......def __str__(self) -> this function is used to display category name like winter instead of default object name like category object 1,category object 2.
