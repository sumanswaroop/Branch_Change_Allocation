from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^bchangeform/', 'form.views.bchangeform', name='bchangeform'),
    
    url(r'^login/$' , 'form.views.login' , name = 'login'),
    url(r'^auth' , 'form.views.auth_view' , name = 'auth_view'),
    url(r'^logout/' , 'form.views.logout' , name = 'logout'),
    
    url(r'^register', 'form.views.register', name = "register"),
    
    url(r'^admin/', include(admin.site.urls)),
) 

if settings.DEBUG :
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)