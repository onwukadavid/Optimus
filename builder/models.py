from django.db import models
from accounts.models import User
from datetime import datetime 

class Template(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    html = models.TextField()
    css = models.TextField()
    thumbnails = models.FileField(default="https://tailwindui.com/img/ecommerce-images/home-page-02-edition-01.jpg", blank=True, null=True)

    def __str__(self):
        return self.name

class UserTemplate(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    html = models.TextField()
    css = models.TextField()
    thumbnails = models.ImageField(null=True, blank=True, default="none")
    created_by = models.ForeignKey(User, related_name='usertemplates', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField( blank=True, default=datetime.now )

    def __str__(self):
        return self.name
