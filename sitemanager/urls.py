from rest_framework import routers
from django.urls import path, include
from sitemanager.views import HomePageViewSet, PartnerViewSet, WhoWeAreViewSet

router = routers.DefaultRouter()
router.register(r'homepage', HomePageViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'whoweare', WhoWeAreViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]