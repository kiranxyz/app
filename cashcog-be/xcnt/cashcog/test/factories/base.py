from factory.alchemy import SQLAlchemyModelFactory

from xcnt.cashcog import db


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session
