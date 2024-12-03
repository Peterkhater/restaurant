from django.db import models

class Gallery(models.Model):
    images = models.ImageField(upload_to='photos', null=False, blank=False)
    text = models.CharField(blank=True, null=True, max_length=200)


class dishCategory(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True)
    note = models.CharField(max_length=50, null=True, blank=True)
    