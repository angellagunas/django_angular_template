# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CatalogueMixin(models.Model):
    """
    Abstract model which define 'name', 'is_active', 'created_date' and
    'last_modified'.
    """
    name = models.CharField(
        max_length=600,
        verbose_name='name'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='is active'
    )

    created_date = models.DateTimeField(
        editable=False,
        blank=True, null=True,
        auto_now_add=True,
        verbose_name=_('created date')
    )

    last_modified = models.DateTimeField(
        editable=False,
        blank=True, null=True,
        auto_now=True,
        verbose_name=_('last modified'),
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ApiModel(CatalogueMixin):
    """
    Abstract model wich define the properties to use drf_scaffolding,
    if a models is extended of this model, then drf_scaffolding will
    generated its API documentation and API endpoints(viewsets, serializers and
    api file).
    """
    class Meta:
        abstract = True

        drf_config = {
            'api': {
                'scaffolding': True
            },
            'serializer': {
                'scaffolding': True
            },
            'form': {
                'scaffolding': False
            },
            'admin': {
                'scaffolding': False
            }
        }
