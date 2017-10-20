from app.catalogs.models import Catalog
from app.models import ApiModel

from django.db import models


class Area(ApiModel):
    """
    Model which define Area schema. An area belongs to a catalog and
    a area has a lot items.
    """
    catalog = models.ForeignKey(
        Catalog,
        related_name="areas"
    )
