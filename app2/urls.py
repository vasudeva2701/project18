from django.urls import path
from app2.views import *
app_name='deva'

urlpatterns=[
    path('app2_second/',app2_second,name='app2_second'),
]