from django.db import models


# Create your models here.

class Serie(models.Model):
    objects: models.query.QuerySet = ...
    
    iframe_link = models.TextField(help_text='The integration iframe link')
    episode = models.IntegerField(help_text='The episode number')
    serie = models.TextField(help_text="The serie's name")