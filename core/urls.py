from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup2, name='signup'),
    url(r'^project_create/$', views.ProjectCreate.as_view(), name='project_create'),
    url(r'^activate/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.activate, name='activate'),
    url(r'^project/(?P<pk>\d+)/detail$', views.ProjectDetail.as_view(), name='project_detail'),
    url(r'^project/(?P<pk>\d+)/donate/$', views.project_donate, name='project_donate'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^blockchainTest/$', views.blockchainTest, name='blockchainTest'),
    url(r'^ProjectAdmin/$', views.ProjectAdmin.as_view(), name='project_admin'),
    url(r'^testDeploy/$', views.testDeploy, name='testDeploy'),
    url(r'^project_update_deploy/$', views.project_update_deploy, name='project_update_deploy'),
    url(r'^project_update_drawdown/$', views.project_update_drawdown, name='project_update_drawdown'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
