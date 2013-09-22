from django.conf.urls import patterns, include, url
from blog.views import blog_post, blog_detail
from . import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myworkspace.views.home', name='home'),
    # url(r'^myworkspace/', include('myworkspace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^blog/$", blog_post, name='blog_post'),
    url(r"^$", views.HomepageView.as_view(), name="home"),
    url(r"^blog/(?P<pk>\d+)/$", blog_detail, name='blog_detail'),
)