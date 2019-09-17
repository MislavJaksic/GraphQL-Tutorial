import pytest

from tests import context
from big_package import server
from graphene.test import Client


@pytest.fixture(scope="module")
def client():
    yield Client(server.schema)


class TestMutations(object):
    @pytest.fixture(scope="class")
    def person(self):
        yield {"name": "Peter", "age": 40}

    @pytest.fixture(scope="function")
    def teardown_database(self):
        yield

        server.faux_database = {}

    def test_create_person_database(self, person, client, teardown_database):
        request = '''mutation {{
                         createPerson(name:"{name}", age:{age}) {{
                             id
                         }}
                     }}'''.format(**person)

        client.execute(request)

        assert server.faux_database != {}

    def test_create_person(self, person, client, teardown_database):
        request = '''mutation {{
                         createPerson(name:"{name}", age:{age}) {{
                            name
                            age
                         }}
                     }}'''.format(**person)

        response = client.execute(request)

        assert response == {
            "data": {
                "createPerson": {
                    "name": person["name"],
                    "age": person["age"]
                }
            }
        }


class TestResolvers(object):
    def test_simple(self, client):
        request = '''{
                         simple
                     }'''

        response = client.execute(request)

        assert response == {
            "data": {
                "simple": "Hello world!"
            }
        }

    @pytest.fixture(scope="class")
    def persons(self):
        persons = []
        persons.append({"name": "Peter", "age": 40})
        persons.append({"name": "Michael", "age": 99})

        yield persons

    @pytest.fixture(scope="class")
    def setup_database(self, persons, client):

        for person in persons:
            request = '''mutation {{
                             createPerson(name:"{name}", age:{age}) {{
                                 id
                             }}
                         }}'''.format(**person)

            client.execute(request)

        yield

        server.faux_database = {}

    def test_person(self, persons, client, setup_database):
        request = '''{
                         allPersons {
                             name
                             age
                         }
                     }'''

        response = client.execute(request)

        assert response == {
            "data": {
                "allPersons": [
                    {
                        "name": persons[0]["name"],
                        "age": persons[0]["age"]
                    },
                    {
                        "name": persons[1]["name"],
                        "age": persons[1]["age"]
                    }
                ]
            }
        }
