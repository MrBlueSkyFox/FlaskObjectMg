import pytest
from sqlalchemy_utils import database_exists, create_database
from app import create_app, db


@pytest.fixture
def app():
    test_config = {"SQLALCHEMY_DATABASE_URI": "postgresql://postgres:Q!w2e3r4t5@localhost:5433/dev2"}
    if not database_exists(test_config["SQLALCHEMY_DATABASE_URI"]):
        create_database(test_config["SQLALCHEMY_DATABASE_URI"])
    app = create_app(test_config)
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
