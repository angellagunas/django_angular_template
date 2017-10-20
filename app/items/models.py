from app.areas.models import Area
from app.models import ApiModel

from django.db import models


class Item(ApiModel):
    """
    Model which define Item schema. An item belongs to an area.
    """
    area = models.ForeignKey(
        Area,
        related_name="items"
    )
