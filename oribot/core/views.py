from django.views.generic import (ListView, DetailView, TemplateView, 
    MonthArchiveView, YearArchiveView)

from .models import Artist, Release, Entry, Daily, Weekly, Yearly

class ArtistListView(ListView):
    queryset = Artist.objects.all()
    template_name = 'artist-list.html'


class ArtistDetailView(DetailView):
    queryset = Artist.objects.all()
    template_name = 'artist-detail'


class ReleaseDetailView(DetailView):
    queryset = Release.objects.all()
    template_name = 'release-detail'

# Don't think we need an Entry Detail because we have Daily/Weekly/Yearly
# but I'm keeping it here so I remember to think about it more later.
# class EntryDetailView(DetailView):
#     queryset = Entry.objects.all()
#     template_name = 'entry-detail'


class DailyListView(ListView):
    queryset = Daily.objects.all()
    template_name = 'daily-list'


class WeeklyListView(ListView):
    queryset = Weekly.objects.all()
    template_name = 'weekly-list'


class YearlyListView(ListView):
    queryset = Yearly.objects.all()
    template_name = 'yearly-list'


class MonthArchiveView(MonthArchiveView):
    queryset = Releases.objects.all()
    template_name = 'month-view'
    date_field = 'released'


class YearArchiveView(YearArchiveView):
    queryset = Release.objects.all()
    template_name = 'year-view'
    date_field = 'released'


class CalendarBrowseView(TemplateView):
    template_name = 'calendar-browse'

    def get_context_data(self, **kwargs):
        context = super(CalendarBrowseView, self).get_context_data(**kwargs)
        context['releases'] = Release.objects.all()
        return context