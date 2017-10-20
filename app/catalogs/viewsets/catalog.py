# -*- coding: utf-8 -*-
from app.catalogs.models import Catalog
from app.catalogs.serializers import catalog as serializers

from soft_drf.api import mixins
from soft_drf.api.viewsets import GenericViewSet


class CatalogViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.PartialUpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = serializers.CatalogSerializer
    list_serializer_class = serializers.CatalogSerializer
    retrieve_serializer_class = serializers.CatalogSerializer
    create_serializer_class = serializers.CatalogSerializer
    update_serializer_class = serializers.CatalogSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Catalog.objects.all()
        return queryset
