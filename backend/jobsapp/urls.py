from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.checking),
    path('register/',views.userregister),
    path('login/',views.login),
    path('jobs/',views.joblist), 
    path('applyjobs/',views.applyjob),
]