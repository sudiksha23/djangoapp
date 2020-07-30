from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import redirect_view
from django.conf.urls.static import static 
from kindling import views
from kindling import models
from kindling import forms
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin', admin.site.urls),
    path("", views.index, name='home'),
    path("index",views.index, name='index'),
    path("login",views.login, name='login'),
    path("entrylogin", views.entrylogin, name="entry"),
    path("searchtable1",views.searchtable1, name="entry"),
    path("searchtable2",views.searchtable2, name="entry"),
    path("searchtable3",views.searchtable3, name="entry"),
    path("searchtable4",views.searchtable4, name="entry"),
    path("ourusers",views.ourusers, name="entry"),
    path("entrysignup", views.entrysignup, name="entry"),
    path("searchin",views.searchin,name="searchin")
    #path("d",views.d, name='d')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)