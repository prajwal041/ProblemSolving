# Flask GraphQL App

A RESTful API built with Flask, GraphQL, Redis, and SQLite3, secured with JWT authentication.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `flask run` or `python3 run.py`

### 1. Get All Users
    curl -X GET http://127.0.0.1:5000/api/users

### 2. Get a Single User by ID
    curl -X GET http://127.0.0.1:5000/api/users/1

### 3. Create a New User
    curl -X POST http://127.0.0.1:5000/api/users \
    -H "Content-Type: application/json" \
    -d '{"username": "john_doe", "email": "john@example.com"}'

### 4. Update a User
    curl -X PUT http://127.0.0.1:5000/api/users/1 \
    -H "Content-Type: application/json" \
    -d '{"username": "john_doe_updated", "email": "john_updated@example.com"}'

### 5. Delete a User
    curl -X DELETE http://127.0.0.1:5000/api/users/1
    

## GraphQL API
### 1. Get all Users
    curl -X POST http://127.0.0.1:5000/graphql/ \
    -H "Content-Type: application/json" \
    -d '{"query": "{ users { id username email } }"}'

### 2. Get a Single User by ID
    curl -X POST http://127.0.0.1:5000/graphql/ \
    -H "Content-Type: application/json" \
    -d '{"query": "{ user(id: 1) { id username email } }"}'

### 3. Create a New User
    curl -X POST http://127.0.0.1:5000/graphql/ \
    -H "Content-Type: application/json" \
    -d '{"query": "mutation { createUser(username: \"john_doe\", email: \"john@example.com\") { user { id username email } } }"}'

### 4. Update a User
    curl -X POST http://127.0.0.1:5000/graphql/ \
    -H "Content-Type: application/json" \
    -d '{"query": "mutation { updateUser(id: 1, username: \"john_doe_updated\", email: \"john_updated@example.com\") { user { id username email } } }"}'

### 5. Delete a User
    curl -X POST http://127.0.0.1:5000/graphql/ \
    -H "Content-Type: application/json" \
    -d '{"query": "mutation { deleteUser(id: 1) { success } }"}'
    