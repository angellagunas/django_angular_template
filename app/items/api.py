# -*- coding: utf-8 -*-
from soft_drf.routing.v1.routers import router

from .viewsets import (
    item,
)


router.register(
    r"items",
    item.ItemViewSet,
    base_name="items",
)
