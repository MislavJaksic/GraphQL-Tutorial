"""
    graphql_server
    ---------------

    An example of a GraphQL server.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
from flask import Flask
from flask_graphql import GraphQLView

import context
from example.server import schema


def main(args):
    """Visit "localhost:5000" to browse the server's API.
    """

    app = Flask(__name__)
    app.add_url_rule("/", view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(debug=True)


def run():
    """Entry point for the runnable script (defined in setup.py)
    """
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run().
    """
    run()
