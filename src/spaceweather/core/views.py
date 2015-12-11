from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions, viewsets, filters

from .forms import ProtonfluxFilter, ElectronfluxFilter, XrayfluxFilter
from .forms import SunspotFilter, SunspotregionFilter
from .forms import AlertFilter

from .models import Protonflux, Ptype, Electronflux, Etype, Xrayflux, Xtype
from .models import Sunspot, Sunspottype, Sunspotregion
from .models import Alert, Alerttype

from .serializers import ProtonfluxSerializer, PtypeSerializer, ElectronfluxSerializer, EtypeSerializer, XrayfluxSerializer, XtypeSerializer
from .serializers import SunspotSerializer, SunspottypeSerializer, SunspotregionSerializer
from .serializers import AlertSerializer, AlerttypeSerializer

User = get_user_model()

class DefaultsMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class ProtonfluxViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Protonflux."""

    queryset = Protonflux.objects.order_by('date')
    serializer_class = ProtonfluxSerializer
    filter_class = ProtonfluxFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class PtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Ptypes."""

    queryset = Ptype.objects.order_by('name')
    serializer_class = PtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)


class ElectronfluxViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Electronflux."""

    queryset = Electronflux.objects.order_by('date')
    serializer_class = ElectronfluxSerializer
    filter_class = ElectronfluxFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class EtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Etypes."""

    queryset = Etype.objects.order_by('name')
    serializer_class = EtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class XrayfluxViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Xrayflux."""

    queryset = Xrayflux.objects.order_by('date')
    serializer_class = XrayfluxSerializer
    filter_class = XrayfluxFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class XtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Xtypes."""

    queryset = Xtype.objects.order_by('name')
    serializer_class = XtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class SunspotViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Sunspots."""

    queryset = Sunspot.objects.order_by('date')
    serializer_class = SunspotSerializer
    filter_class = SunspotFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class SunspottypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Sunspottypes."""

    queryset = Sunspottype.objects.order_by('name')
    serializer_class = SunspottypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class SunspotregionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Sunspot Regions."""

    queryset = Sunspotregion.objects.order_by('date')
    serializer_class = SunspotregionSerializer
    filter_class = SunspotregionFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'region',)

class AlerttypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Alerttypes."""

    queryset = Alerttype.objects.order_by('name')
    serializer_class = AlerttypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class AlertViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Alerts."""

    queryset = Alert.objects.order_by('issuetime')
    serializer_class = AlertSerializer
    filter_class = AlertFilter
    search_fields = ('issuetime',)
    ordering_fields = ('issuetime', 'name',)
