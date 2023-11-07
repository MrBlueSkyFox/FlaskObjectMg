from pathlib import Path
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.explorer.playground import PLAYGROUND_HTML
import click
from flask import Flask, g, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .queries import get_object
from .mutations import set_object_pool, free_object

type_defs = load_schema_from_path("schema.graphql")
query_type = ObjectType("Query")
mutation_type = ObjectType("Mutation")

query_type.set_field("getObject", get_object)
mutation_type.set_field("setObjectPool", set_object_pool)
mutation_type.set_field("freeObject", free_object)
# @query_type.field("hello")
# def get_hello(*_):
#     return "hello"


# query_type.set_field("getTest", get_test)
# query_type.set_field("hello", get_hello)

schema = make_executable_schema(
    type_defs, query_type, mutation_type
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    Path("instance").mkdir(exist_ok=True)
    CORS(app)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    db.init_app(app)

    @app.route("/graphql", methods=["GET"])
    def graphql_playground():
        return PLAYGROUND_HTML, 200

    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        data = request.get_json()
        success, result = graphql_sync(
            schema,
            data,
            context_value=request,
            debug=app.debug
        )
        status_code = 200 if success else 400
        return jsonify(result), status_code

    from .object_mgr import object_mgr_bp
    app.register_blueprint(object_mgr_bp.bp)
    app.cli.add_command(init_db_command)
    return app


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    click.echo('Initialized the database.')
