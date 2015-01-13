from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django_kss.views import AutoStyleGuideView

admin.autodiscover()


class StyleGuideView(AutoStyleGuideView):
    template_name = 'main-style-guide.html'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uber.views.home', name='home'),
    # url(r'^uber/', include('uber.foo.urls')),

    url(r'^$', TemplateView.as_view(template_name='uber.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^style_guide/(?P<section>\d*)$', StyleGuideView.as_view(), name='styleguide'),
)
