# -*- coding: utf-8 -*-
from app.items.models import Item
from app.items.serializers import item as serializers

from soft_drf.api import mixins
from soft_drf.api.viewsets import GenericViewSet


class ItemViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.PartialUpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = serializers.ItemSerializer
    list_serializer_class = serializers.ItemSerializer
    retrieve_serializer_class = serializers.ItemSerializer
    create_serializer_class = serializers.ItemSerializer
    update_serializer_class = serializers.ItemSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Item.objects.all()
        return queryset
