from rest_framework import routers
from django.urls import path, include
from sitemanager.views import HomePageViewSet

router = routers.DefaultRouter()
router.register(r'homepage', HomePageViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]