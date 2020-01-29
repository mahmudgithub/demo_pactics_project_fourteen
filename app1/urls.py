#from django.conf.urls import path
#from . import views

#urlpatterns = [
#    path('add/blog/', views.add_blog, name='add_blog'),
#]

from django.urls import path
from . import views

urlpatterns = [
path('add/blog/',views.add_blog,name='add_blog'),
path('edit/blog/(?P<id>\d+)/', views.edit_blog, name='edit_blog'),
]