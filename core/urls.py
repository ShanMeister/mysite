from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup2, name='signup'),
    url(r'^project_create/$', views.ProjectCreate.as_view(), name='project_create'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^project/(?P<pk>\d+)/detail$', views.ProjectDetailView.as_view(), name='project_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)