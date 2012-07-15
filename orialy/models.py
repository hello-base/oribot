from django.db import models


class Release(models.Model):
    pass


class Entry(models.Model):
    sales = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)


class Daily(Entry):
    release = models.ForeignKey(Release, related_name='dailies')


class Weekly(Entry):
    release = models.ForeignKey(Release, related_name='weeklies')


class Yearly(Entry):
    release = models.ForeignKey(Release, related_name='yearlies')
