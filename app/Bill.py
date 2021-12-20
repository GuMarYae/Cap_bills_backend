"""Bill Model."""

from masoniteorm.models import Model


class Bill(Model):
    __table__="bills"