# -*- coding: utf-8 -*-
from app.areas.serializers.area import AreaSerializer
from app.items.models import Item

from soft_drf.api.serializers import ModelSerializer


class ItemSerializer(ModelSerializer):

    area = AreaSerializer(many=False)

    class Meta:
        model = Item
        fields = (
            'id',
            'name',
            'is_active',
            'area',
        )
