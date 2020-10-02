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
    path("login",views.login, name='login'),
    path("", views.index, name='home'),
    path("index",views.index, name='index'),
    path("entrylogin", views.entrylogin, name="entry"),
    path("searchtable1",views.searchtable1, name="entry"),
    path("searchtable2",views.searchtable2, name="entry"),
    path("searchtable3",views.searchtable3, name="entry"),
    path("searchtable4",views.searchtable4, name="entry"),
    #path("filters",views.filters, name="filters"),
    path("ourusers",views.ourusers, name="entry"),
    path("entrysignup", views.entrysignup, name="entry"),
    path("searchin",views.searchin,name="searchin"),
    #path("profile",views.profile,name="profile"),
    path("profile/<str:pk_test>",views.profile, name="profile"),
    path("update/<str:pk>",views.update, name="update"),
    path("delete/<str:pk2>",views.delete, name="delete"),
    
    #path("d",views.d, name='d')
    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)