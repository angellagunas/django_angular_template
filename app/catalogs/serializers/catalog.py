# -*- coding: utf-8 -*-
from app.catalogs.models import Catalog

from soft_drf.api.serializers import ModelSerializer


class CatalogSerializer(ModelSerializer):

    class Meta:
        model = Catalog
        fields = (
            'id',
            'name',
            'is_active',
        )
