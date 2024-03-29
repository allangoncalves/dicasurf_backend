from django.conf.urls import url, include
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter
from api.views import CityViewSet, SpotViewSet, StateViewSet, NearestSpotViewSet, PostViewSet, FirstUserViewSet, PossiblePartnerViewSet

router = SimpleRouter()
router.register(r'firstusers', FirstUserViewSet)
router.register(r'possiblepartners', PossiblePartnerViewSet)
router.register(r'states', StateViewSet, base_name="states")
router.register(r'posts', PostViewSet, base_name="posts")
router.register(r'nearest', NearestSpotViewSet, base_name="nearest")


state_router = routers.NestedDefaultRouter(router, r'states', lookup="state")
state_router.register(r'cities', CityViewSet, base_name="state-cities")

cities_router = routers.NestedSimpleRouter(state_router, r'cities', lookup="city")
cities_router.register(r'spots', SpotViewSet, base_name="cities-spots")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(state_router.urls)),
    url(r'^', include(cities_router.urls))
]