# -*- coding: utf-8 -*-
from soft_drf.routing.v1.routers import router

from .viewsets import (
    catalog,
)


router.register(
    r"catalogs",
    catalog.CatalogViewSet,
    base_name="catalogs",
)
