# -*- coding: utf-8 -*-
from app.areas.models import Area
from app.catalogs.serializers.catalog import CatalogSerializer

from soft_drf.api.serializers import ModelSerializer


class AreaSerializer(ModelSerializer):

    catalog = CatalogSerializer(many=False)

    class Meta:
        model = Area
        fields = (
            'id',
            'name',
            'is_active',
            'catalog',
        )
