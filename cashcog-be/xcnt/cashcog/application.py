import os
from http import HTTPStatus

import flask_cors
from flask import Flask, request, Response
from flask_graphql import GraphQLView
from .schema import schema

app = Flask("xcnt.cashcog")


class DecoratedGraphQLView(GraphQLView):
    methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

    decorators = (
        flask_cors.cross_origin(
            origins=[
                item.strip() for item in os.getenv("ALLOWED_CORS_ORIGINS", "*").split(",")
            ],
            expose_headers=["Content-Type"],
            support_credentials=True,
        ),
    )

    def dispatch_request(self):
        request_method = request.method.lower()
        if request_method == "options":
            return Response(status=HTTPStatus.NO_CONTENT)
        return super().dispatch_request()


@app.route("/", methods=["GET"])
def index():
    return "Hello World"


app.add_url_rule("/graphql", view_func=DecoratedGraphQLView.as_view("graphql", schema=schema, graphiql=True))
