from django.db import models
from django.db.models import Max, Sum

from model_utils import Choices


class Artist(models.Model):
    pass


class Release(models.Model):
    KIND = Choices(('album', 'Album'), ('single', 'Single'))

    kind = models.CharField(choices=KIND, default=KIND.single, max_length=6)
    artist = models.ForeignKey(Artist)

    name = models.CharField(max_length=255)
    kanji = models.CharField(max_length=255)
    released = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.name)

    def sales(self):
        return self.weeklies.annotate(total=Sum('sales'))

    def highest_weekly_rank(self):
        return self.weeklies.annotate(total=Max('rank'))


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
    date_starting = models.DateField()

    def __unicode__(self):
        return u'%s: Year' % (self.release.name)
