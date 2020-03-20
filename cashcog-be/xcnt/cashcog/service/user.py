from loguru import logger
from uuid import UUID

from xcnt.cashcog.database import db
from xcnt.cashcog.models import User
from validate_email import validate_email


class InvalidEmailException(ValueError):
    pass


class UserAlreadyExistsException(ValueError):
    pass


class UserDoesNotExistException(ValueError):
    pass


class InvalidUUIDException(ValueError):
    pass


def create_user(user_input_data: User):
    email = user_input_data.email.lower()
    if not validate_email(email):
        raise InvalidEmailException(user_input_data)

    user = db.session.query(User).filter(User.email == email).first()
    if user is not None:
        raise UserAlreadyExistsException(user_input_data)

    logger.debug(f"Creating new user with email: {email}")

    user = User(
        email=email,
        first_name=user_input_data.first_name,
        last_name=user_input_data.last_name,
        newsletter=user_input_data.newsletter
    )
    db.session.add(user)
    return user


def update_user(user_input_data: User):
    email = user_input_data.email.lower()
    if not validate_email(email):
        raise InvalidEmailException(user_input_data)

    uuid = user_input_data.uuid
    if not _validate_uuid(uuid):
        raise InvalidUUIDException(user_input_data)

    user = db.session.query(User).filter(User.uuid == user_input_data.uuid).first()
    if user is None:
        raise UserDoesNotExistException(user_input_data)

    user_email_exists = db.session.query(User).filter(
        User.email == user_input_data.email,
        User.uuid != user_input_data.uuid
    ).first()
    if user_email_exists is not None:
        raise UserAlreadyExistsException(user_input_data)

    logger.debug(f"Updating user with email: {email}")

    user.email = user_input_data.email
    user.first_name = user_input_data.first_name
    user.last_name = user_input_data.last_name
    user.newsletter = user_input_data.newsletter

    db.session.commit()
    return user


def delete_user(uuid: str):
    user = db.session.query(User).filter(User.uuid == uuid).first()
    db.session.delete(user)
    db.session.commit()


def _validate_uuid(uuid: str):
    try:
        UUID(uuid)
        return True
    except ValueError:
        return False