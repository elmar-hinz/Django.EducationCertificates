# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    rank = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('rank',)

class Certificate(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    file = models.FileField()
    url_to_certificate = models.URLField(blank=True)
    url_to_course = models.URLField(blank=True)
    teachers = models.CharField(max_length=256, blank=True)
    school = models.CharField(max_length=256, blank=True)
    provider = models.CharField(max_length=256, blank=True)
    date_of_earning = models.DateField(null=True, blank=True)
    date_of_expiration = models.DateField(null=True, blank=True)
    rank = models.PositiveSmallIntegerField(null=True, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('rank',)


