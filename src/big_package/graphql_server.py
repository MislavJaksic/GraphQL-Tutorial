from graphene import ObjectType, Field, ID, String, Int, Schema, Mutation, Argument
import uuid


class Query(ObjectType):
    """
    type Query {
        hello(name: String = "stranger"): String
        goodbye: String
    }
    """

    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        print("=== START ===")
        print(root)
        print(info.context)
        print(name)
        print("=== END ===")
        return f"Hello {name}!"

    def resolve_goodbye(root, info):
        return "See ya!"


class Person(ObjectType):
    """
    type Person {
      name: String!
      age: Int!
      posts: [Post!]!
    }
    """

    id = Field(ID)
    name = Field(String)
    age = Field(Int)

    def resolve_id(root, info):
        return id

    def resolve_name(root, info):
        return name

    def resolve_age(root, info):
        return age


class CreatePerson(Mutation):
    id = Field(ID)
    name = Field(String)
    age = Field(Int)

    class Arguments:
        name = Argument(String)
        age = Argument(Int)

    def mutate(self, info, name, age):
        id = uuid.uuid4()
        person = Person(id, name, age)

        return CreatePerson(person.id, person.name, person.age)


class Mutation(ObjectType):
    create_person = CreatePerson.Field()


class Post(ObjectType):
    """
    type Post {
      text: String!
      author: Person!
    }
    """

    id = ID()
    text = String()


schema = Schema(query=Query)

schema_2 = Schema(query=Person, mutation=Mutation)  # TODO, see graphite mutations (Person/=Query)
