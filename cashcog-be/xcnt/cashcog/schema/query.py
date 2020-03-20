import graphene
from xcnt.cashcog.schema.objects import User


class Query(graphene.ObjectType):
    users = graphene.List(
        User,
        first=graphene.Int(),
        skip=graphene.Int(),
    )

    def resolve_users(self, info, first=None, skip=None, **kwargs):
        users = User.get_query(info).all()

        if skip:
            users = users[skip:]

        if first:
            users = users[:first]

        return users
