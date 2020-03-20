import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from xcnt.cashcog.models import User as _User


class UserAttributes():
    email = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    newsletter = graphene.Boolean(required=True)


class User(SQLAlchemyObjectType):
    class Meta:
        model = _User


class CreateUserInput(graphene.InputObjectType, UserAttributes):
    pass


class UpdateUserInput(graphene.InputObjectType, UserAttributes):
    uuid = graphene.String(required=True)
