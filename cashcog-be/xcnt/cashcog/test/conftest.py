import pytest
import os

from alembic import command
from alembic.config import Config
from dotenv import load_dotenv, find_dotenv
from loguru import logger

from xcnt.cashcog import app as flask_app, init_app, db
from xcnt.cashcog.database import ROOT_PATH


def init_if_not_done():
    if not getattr(app, "_initialized", False):
        init_app()
        setattr(app, "_initialized", True)


@pytest.fixture(scope="session")
def app():
    logger.disable("")
    load_dotenv(find_dotenv())
    if os.getenv("ENV") != "test":
        raise RuntimeError("Set environment variable to env")
    app_object = flask_app.test_client()
    yield app_object


@pytest.fixture(scope="session")
def alembic_config():
    config = Config(file_="alembic.ini", ini_section="alembic")
    config.attributes["configure_logger"] = False
    config.set_main_option("script_location", os.path.join(ROOT_PATH, "alembic"))
    return config


@pytest.fixture
def database(app, alembic_config):
    """
    Prepares a database on a per test basis
    """
    with flask_app.app_context():
        command.downgrade(alembic_config, "base")
        command.upgrade(alembic_config, "head")
    init_if_not_done()
    yield db.session


@pytest.fixture
def client(app, database):
    """
    Returns the initialized flask testing context
    """
    context = flask_app.app_context()
    context.push()
    yield app
    context.pop()
