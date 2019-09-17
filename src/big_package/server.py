from graphene import ObjectType, Field, NonNull, ID, String, Int, List, Schema, Mutation, Argument
import uuid


faux_database = {}


class Person(ObjectType):
    """
    type Person {
        id: String!
        name: String!
        age: Int
        # posts: [Post!]!
    }
    """
    id = NonNull(ID)
    name = NonNull(String)
    age = Field(Int)


class CreatePerson(Mutation):
    id = NonNull(ID)
    name = NonNull(String)
    age = Field(Int)

    class Arguments:
        name = Argument(String)
        age = Argument(Int)

    def mutate(root, info, name, age):
        id = uuid.uuid4()
        faux_database[id] = Person(id=id, name=name, age=age)

        return CreatePerson(id=id, name=name, age=age)


class MyMutations(ObjectType):
    create_person = CreatePerson.Field()


class Query(ObjectType):
    simple = Field(String)

    all_persons = List(Person, name=String())

    def resolve_simple(parent, info):
        return "Hello world!"

    def resolve_all_persons(parent, info, **kwargs):
        values = faux_database.values()
        # if name:
        #     values = map(lambda x: x["Name"] == name, values)
        return values


schema = Schema(query=Query, mutation=MyMutations)
