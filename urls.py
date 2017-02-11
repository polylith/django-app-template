from django.conf.urls import url, include
from rest_framework import routers
from {{ app_name }} import api

router = routers.DefaultRouter()
# Add your router.register calls here

urlpatterns = [
    url(r'^api/', include(router.urls)),
]