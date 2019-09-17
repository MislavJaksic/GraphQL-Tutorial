"""
    Project-Name.py
    ---------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
from flask import Flask
from flask_graphql import GraphQLView

import context
from big_package.server import schema


def main(args):
    """main will be run if you run this script directly
    """

    app = Flask(__name__)
    app.add_url_rule(
      '/',
      view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )
    app.run()


def run():
    """Entry point for the runnable script (defined in setup.py)
    """
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run().
    """
    run()
