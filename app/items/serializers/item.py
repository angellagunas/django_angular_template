# -*- coding: utf-8 -*-
from app.items.models import Item

from soft_drf.api.serializers import ModelSerializer


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = (
            'id',
            'name',
            'is_active',
            'area',
        )
