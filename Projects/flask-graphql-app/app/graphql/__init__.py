from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

bp = Blueprint('graphql', __name__, url_prefix='/graphql')

bp.add_url_rule(
    '/',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)