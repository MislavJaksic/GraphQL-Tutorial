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
# Note: '!' fields are non-null, [] is an array
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

```
mutation {
  createPerson(name: "Bob", age: 36) {
    name
    age
  }
}
```

```
subscription {
  newPerson {
    name
    age
  }
}
```

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
```

### Big Picture (Architecture)

Use cases:  
1) expose data in a database (AWS Aurora/MongoDB/...)
2) integrates existing systems (legacy/microservice/third-party/...)
3) mix of 1) and 2)

Resolver function is responsible for fetching the data.  
The server will package all the data and send it as a response.  

### Clients

### Server

### More GraphQL Concepts

### Tooling and Ecosystem

### Security

### Common Questions
