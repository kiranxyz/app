from __future__ import annotations

import factory
from uuid import uuid4

from xcnt.cashcog.models import User
from .base import BaseFactory


class UserFactory(BaseFactory):
    class Meta:
        model = User

    uuid = factory.LazyFunction(uuid4)
    email = factory.Sequence(lambda x: f"user{x}@example.com")
    first_name = factory.Sequence(lambda x: f"first_name{x}")
    last_name = factory.Sequence(lambda x: f"last_name{x}")
    newsletter = False
