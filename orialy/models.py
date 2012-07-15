from django.db import models
from django.db.models import Sum


class Release(models.Model):
    def __unicode__(self):
        return u'%s' % (self.name)

    def daily_sales(self):
        return self.dailies.annotate(total=Sum('sales'))


class Entry(models.Model):
    sales = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class Daily(Entry):
    release = models.ForeignKey(Release, related_name='dailies')
    date = models.DateField()

    def __unicode__(self):
        return u'%s: Daily for %s' % (self.release.name, self.date)


class Weekly(Entry):
    release = models.ForeignKey(Release, related_name='weeklies')
    date_starting = models.DateField()
    date_ending = models.DateField()

    def __unicode__(self):
        return u'%s: Week of %s' % (self.release.name, self.date_starting)


class Yearly(Entry):
    release = models.ForeignKey(Release, related_name='yearlies')

    def __unicode__(self):
        return u'%s: Year' % (self.release.name)
