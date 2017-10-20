# -*- coding: utf-8 -*-
from app.areas.models import Area

from soft_drf.api.serializers import ModelSerializer


class AreaSerializer(ModelSerializer):

    class Meta:
        model = Area
        fields = (
            'id',
            'name',
            'is_active',
            'catalog',
        )
