"""
    Project-Name.py
    ---------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys

import context
from big_package import graphql_server


def main(args):
    """main will be run if you run this script directly
    """

    # we can query for our field (with the default argument)
    query_string = "{ hello }"
    result = graphql_server.schema.execute(query_string)
    print(result.data["hello"])
    # "Hello stranger"

    # or passing the argument in the query
    query_with_argument = '{ hello(name: "GraphQL") }'  # INNER QUOTES MUST BE DOUBLE!
    result = graphql_server.schema.execute(query_with_argument)
    print(result.data["hello"])
    # "Hello GraphQL!"

    create_string = 'mutation { createPerson(name: "Gani", age: "40") { id } }'
    result = graphql_server.schema_2.execute(create_string)
    print(result.data)


def run():
    """Entry point for the runnable script (defined in setup.py)
    """
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run().
    """
    run()
