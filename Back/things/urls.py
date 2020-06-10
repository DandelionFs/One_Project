from django.urls import path

from things.views import listthings
from things import manage

urlpatterns = [

    path('manage/', manage.dispatcher),
    path('list/', listthings),


]