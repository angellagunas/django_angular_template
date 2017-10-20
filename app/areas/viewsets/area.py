# -*- coding: utf-8 -*-
from app.areas.models import Area
from app.areas.serializers import area as serializers

from soft_drf.api import mixins
from soft_drf.api.viewsets import GenericViewSet


class AreaViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.PartialUpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = serializers.AreaSerializer
    list_serializer_class = serializers.AreaSerializer
    retrieve_serializer_class = serializers.AreaSerializer
    create_serializer_class = serializers.AreaSerializer
    update_serializer_class = serializers.AreaSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Area.objects.all()
        return queryset
