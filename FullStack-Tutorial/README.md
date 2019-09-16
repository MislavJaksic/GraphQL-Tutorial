## [Fullstack Tutorial for GraphQL](https://www.howtographql.com/)

### Introduction

API defines how a client can load data from a server.  
GraphQL is a query language for APIs.  

### GraphQL is better then REST

GraphQL is better then REST:
* get data with a single request
* has a precise schema and type system
* quick to develop

REST is server efficient while GraphQL is client friendly.  

### Core Concepts

```
Schema
Type
Field

Root field (of the query)
Payload (of the query)

Mutations: create, update, delete

Subscription
```

#### Schema Definition Language (SDL)
```
type Type-Name {
  Field-Name1: Type-Name!
  Field-Name2: [Type-Name]
}

# Note: "!" fields are non-null, [] is an array
```

Define a 1-N relationship:
```
type Post {
  title: String!
  author: Person!
}
type Person {
  name: String!
  age: Int!
  posts: [Post!]!
}
```

#### Query

```
{
  Root-Field (_argument: _value) {
    _payload
  }
}
```

```
{
  allPersons (last: 2) {
    name
    age
    posts {
      title
    }
  }
}
```

#### Mutations

```
mutation {
  createPerson(name: "Bob", age: 36) {
    name
    age
  }
}
```

#### Subscription

```
subscription {
  newPerson {
    name
    age
  }
}
```

#### Schema

```
type Query {
  allPersons(last: Int): [Person!]!
}

type Mutation {
  createPerson(name: String!, age: Int!): Person!
}

type Subscription {
  newPerson: Person!
}

type Person {
  name: String!
  age: Int!
  posts: [Post!]!
}

type Post {
  title: String!
  author: Person!
}

# Note: Query, Mutation, and Subscription types are the entry points
# Note: allPersons, createPerson and newPerson are root field
```

### Big Picture (Architecture)

GraphQL is a specification.  

Use cases:  
1) expose data in a database (AWS Aurora/MongoDB/...)
2) integrates existing systems (legacy/microservice/third-party/...)
3) mix of 1) and 2)

Resolver function is responsible for fetching the data for a field.  
The server will package all the data and send it as a response.  

```
query {
  User(id: _value) {
    name
    friends(first: 5) {
      name
      age
    }
  }
}
```

```
User(id: String!): User
name(user: User!): String!
age(user: User!): Int!
friends(first: Int, user: User!): [User!]!
```

### Clients

Don't have to worry about over or under fetching data.

### Server

### More GraphQL Concepts

### Tooling and Ecosystem

### Security

### Common Questions
