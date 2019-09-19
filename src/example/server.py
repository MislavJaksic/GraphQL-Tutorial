from graphene import ObjectType, Schema, Mutation
from graphene import Field, Argument, NonNull, List
from graphene import ID, String, Int
import uuid


faux_database = {}


class Person(ObjectType):
    """User which can author posts.
    """
    """
    type Person {
        id: ID!
        name: String!
        age: Int
        # posts: [Post!]!
    }
    """
    id = NonNull(ID, description="Unique ID.")
    name = NonNull(String, description="Name, full name or username.")
    age = Field(Int, description="Age in years.")


class Post(ObjectType):
    """A text published by an author.
    """
    """
    type Post {
        id: ID!
        text: String!
        author: Person!
    }
    """
    id = NonNull(ID, description="Unique ID.")
    text = NonNull(String, description="UTF-8 content.")
    author = NonNull(Person, description="Text author.")


class CreatePerson(Mutation):
    """Create a new person.
    """
    # class Meta(object):
    #     interfaces = (Person, )  # TODO: REFACTOR!
    id = NonNull(ID, description="Unique ID.")
    name = NonNull(String, description="Name, full name or username.")
    age = Field(Int, description="Age in years.")
    # person = Field(Person)  # TODO

    class Arguments:
        name = Argument(String, required=True, description="Name, full name or username.")
        age = Argument(Int, default_value=-1, description="Age in years.")

    def mutate(root, info, name, **kwargs):
        id = uuid.uuid4()
        age = kwargs.get("age")
        person = Person(id=id, name=name, age=age)

        faux_database[id] = person

        return CreatePerson(id=id, name=name, age=age)
        # return CreatePerson(person=person)


class Mutations(ObjectType):
    """A GraphQL-Flask mutation example.
    """
    create_person = CreatePerson.Field()


class Query(ObjectType):
    """A GraphQL-Flask query example.
    """
    simple = Field(String, description="'Hello world!' example.")

    all_persons = List(Person, name=String(), description="List every person.")

    def resolve_simple(parent, info):
        return "Hello world!"

    def resolve_all_persons(parent, info, **kwargs):
        values = faux_database.values()

        name = kwargs.get("name")
        if name:
            values = filter(lambda x: name in x.name, values)

        return values


schema = Schema(query=Query, mutation=Mutations, auto_camelcase=True)
