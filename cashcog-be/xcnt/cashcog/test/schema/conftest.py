import pytest

from graphene.test import Client

from xcnt.cashcog.schema import schema


@pytest.fixture
def graphql_client(client):
    return Client(schema)
