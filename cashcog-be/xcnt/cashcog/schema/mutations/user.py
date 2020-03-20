import graphene
from loguru import logger
from xcnt.cashcog.schema.objects import User, CreateUserInput, UpdateUserInput
from xcnt.cashcog.database import db
from xcnt.cashcog.service.user import (
    create_user,
    update_user,
    delete_user,
    UserAlreadyExistsException,
    InvalidEmailException,
    UserDoesNotExistException,
    InvalidUUIDException
)


class UserError(graphene.Enum):
    INVALID_EMAIL = 1
    ALREADY_CREATED = 2
    DOES_NOT_EXIST = 3
    INVALID_UUID = 4

    @property
    def description(self):
        if self == UserError.INVALID_EMAIL:
            return "Entered user email is invalid"
        if self == UserError.ALREADY_CREATED:
            return "The email for this user has already been used"
        if self == UserError.DOES_NOT_EXIST:
            return "User with this uuid does not exist"
        elif self == UserError.INVALID_UUID:
            return "Provided uuid is invalid"


class CreateUser(graphene.Mutation):
    class Arguments:
        input = CreateUserInput(required=True)

    ok = graphene.Boolean()
    error = UserError()
    user = graphene.Field(User)

    def mutate(self, root, input):
        try:
            user = create_user(input)
        except InvalidEmailException:
            return CreateUser(ok=False, error=UserError.INVALID_EMAIL, user=None)
        except UserAlreadyExistsException:
            return CreateUser(ok=False, error=UserError.ALREADY_CREATED, user=None)
        db.session.commit()
        return CreateUser(ok=True, error=None, user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        input = UpdateUserInput(required=True)

    ok = graphene.Boolean()
    error = UserError()
    user = graphene.Field(User)

    def mutate(self, root, input):
        try:
            user = update_user(input)
        except InvalidEmailException:
            return UpdateUser(ok=False, error=UserError.INVALID_EMAIL, user=None)
        except UserDoesNotExistException:
            return UpdateUser(ok=False, error=UserError.DOES_NOT_EXIST, user=None)
        except UserAlreadyExistsException:
            return UpdateUser(ok=False, error=UserError.ALREADY_CREATED, user=None)
        except InvalidUUIDException:
            return UpdateUser(ok=False, error=UserError.INVALID_UUID, user=None)
        return UpdateUser(ok=True, error=None, user=user)


class DeleteUser(graphene.Mutation):
    class Arguments:
        uuid = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(self, root, uuid):
        try:
            delete_user(uuid)
        except Exception as e:
            logger.error(e)
        return DeleteUser(ok=True)
