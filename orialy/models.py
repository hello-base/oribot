from django.db import models
from django.db.models import Sum


class Release(models.Model):
    def daily_sales(self):
        return self.dailies.annotate(total=Sum('sales'))


class Entry(models.Model):
    sales = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class Daily(Entry):
    release = models.ForeignKey(Release, related_name='dailies')


class Weekly(Entry):
    release = models.ForeignKey(Release, related_name='weeklies')


class Yearly(Entry):
    release = models.ForeignKey(Release, related_name='yearlies')
