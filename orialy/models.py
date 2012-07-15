from django.db import models


class Release(models.Model):
    pass


class Entry(models.Model):
    sales = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)


class Weekly(models.Model):
    pass


class Yearly(models.Model):
    pass
