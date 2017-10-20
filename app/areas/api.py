# -*- coding: utf-8 -*-
from soft_drf.routing.v1.routers import router

from .viewsets import (
    area,
)


router.register(
    r"areas",
    area.AreaViewSet,
    base_name="areas",
)
