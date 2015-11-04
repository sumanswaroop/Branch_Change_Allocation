from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^bchangeform', 'form.views.bchangeform', name='bchangeform'),
    url(r'^login/$' , 'form.views.login' , name = 'login'),
    url(r'^auth' , 'form.views.auth_view' , name = 'auth_view'),
    url(r'^logout' , 'form.views.logout' , name = 'logout'),

    url(r'^register', 'form.views.register', name = "register"),
    url(r'^registersuccess', 'form.views.registersuccess', name = "registersuccess"),
    url(r'^success', 'form.views.success', name = "success"),
    url(r'^fdetail', 'form.views.fdetail', name = "fdetail"),
    url(r'^admin/programs/','form.views.showprograms',name="programs"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/getAllocation/','form.views.generateoutput',name='output'),
    url(r'^admin/getStats/','form.views.generatestats',name='stats'),
    url(r'^$' , 'form.views.login' , name = 'login'),
)

if settings.DEBUG :
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
