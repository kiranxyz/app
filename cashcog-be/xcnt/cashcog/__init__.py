from dotenv import load_dotenv, find_dotenv
from .application import app
from .database import db, get_url


def init_app():
    load_dotenv(find_dotenv())
    url = get_url()
    app.config["SQLALCHEMY_DATABASE_URI"] = url
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    db.init_app(app)

    return app
