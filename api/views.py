from rest_framework import viewsets, pagination, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from django.db.models.expressions import RawSQL
from api.serializers import *

# Create your views here.

class FirstUserViewSet(viewsets.ModelViewSet):
    serializer_class = FirstUserSerializer
    queryset = FirstUser.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'list' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
class NearestSpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotAndCitySerializer

    def get_queryset(self):
        lat = self.request.query_params.get("lat", 0)
        lng = self.request.query_params.get("lng", 0)
        """
        Return objects sorted by distance to specified coordinates
        which distance is less than max_distance given in kilometers
        """
        # Great circle distance formula
        gcd_formula = "6371 * acos(least(greatest(\
        cos(radians(%s)) * cos(radians(lat)) \
        * cos(radians(lng) - radians(%s)) + \
        sin(radians(%s)) * sin(radians(lat)) \
        , -1), 1))"
        distance_raw_sql = RawSQL(
            gcd_formula,
            (lat, lng, lat)
        )
        return Spot.objects.all() \
        .annotate(distance=distance_raw_sql)\
        .order_by('distance')

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class PostViewSet(viewsets.ModelViewSet):
    serializers = {
        'list': PostPreviewSerializer,
        'others': PostSerializer
    }
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text', 'preview_text']
    pagination_class = pagination.LimitOffsetPagination
    
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['others'])
    
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotDetailSerializer

    def get_queryset(self):
        return SpotDetail.objects.filter(spot__city=self.kwargs['city_pk'])

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_visible',]

    def get_queryset(self):
        return City.objects.filter(state=self.kwargs['state_pk'])

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_visible',]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
