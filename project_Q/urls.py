#from django.conf.urls import url, include
#from django.contrib import admin

#urlpatterns = [
 #   url(r'^admin/', admin.site.urls),
 #   url(r'go/', include('app1.urls')),
#]

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('go/',include('app1.urls')),
]