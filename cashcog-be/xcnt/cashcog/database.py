import os
import time
from alembic import command
from alembic.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), *(("..",) * 2)))
db = SQLAlchemy(engine_options=dict(pool_recycle=3600))
os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"] = "false"


def is_empty_or_none(value):
    return value is None or (isinstance(value, str) and len(value) == 0)


def get_url():
    url_input = [os.getenv("DB_USER", "postgres")]
    url = "postgresql://%s"
    password = os.getenv("DB_PASSWORD", None)
    if not is_empty_or_none(password):
        url_input.append(password)
        url += ":%s"
    url += "@%s"
    url_input.append(os.getenv("DB_HOST", "localhost"))
    port = os.getenv("DB_PORT", None)
    if not is_empty_or_none(port):
        url += ":%s"
        url_input.append(port)
    url += "/%s"
    url_input.append(os.getenv("DB_NAME", "postgres"))

    return url % tuple(url_input)


def run_migrations():
    config = Config(file_="alembic.ini", ini_section="alembic")
    config.set_main_option("script_location", os.path.join(ROOT_PATH, "alembic"))
    command.upgrade(config, "head")


def run_connection_check(remaining_tries=10):
    sqlalchemy_url = get_url()
    retry = False
    connection = None
    try:
        engine = create_engine(sqlalchemy_url)
        connection = engine.connect()
    except exc.OperationalError:
        retry = True
        if remaining_tries == 0:
            raise
    finally:
        if connection is not None:
            connection.close()

    if retry:
        print("No connection to database. Waiting 5 seconds")
        time.sleep(5)
        run_connection_check(remaining_tries - 1)
