from django.conf.urls import patterns, url

from .views import (ArtistListView, ArtistDetailView, ReleaseDetailView, 
    DailyListView, WeeklyListView, YearlyListView, CalendarBrowseView, 
    MonthArchiveView, YearArchiveView)


urlpattern = patterns('',
    url(r'^artist/(?P<slug>[-\w]+)/$', name='artist-detail', view=ArtistDetailView.as_view()),
    url(r'^artist/$', name='artist-list', view=ArtistListView.as_view()),
    
    url(r'^release/(?P<slug>[-\w]+)/$', name='release-detail', view=ReleaseDetailView.as_view()),
    
    url(r'^daily/$', name='daily-list', view=DailyListView.as_view()),
    
    url(r'^weekly/$', name='weekly-list', view=WeeklyListView.as_view()),
    
    url(r'^yearly/$', name='yearly-list', view=YearlyListView.as_view()),
    
    url(r'^calendar/$', name='calendar-browse', view=CalendarBrowseView.as_view()),
    
    url(r'^(?P<month>\d{2})/$', name='month-view', view=MonthArchiveView.as_view()),
    
    url(r'^(?P<year>\d{4})/$') name='year-view', view=YearArchiveView.as_view(),
)