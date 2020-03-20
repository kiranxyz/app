import graphene
from .user import CreateUser, UpdateUser, DeleteUser


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
