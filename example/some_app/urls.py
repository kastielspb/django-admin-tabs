from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^some/catalog/some/table-very-big/$', SomePageView.as_view(), name='some_page')
]
