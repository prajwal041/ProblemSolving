import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models import User
from .. import db

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_users(self, info):
        return User.query.all()

    def resolve_user(self, info, id):
        return User.query.get(id)

# Define the Mutation class
class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)

# Define the UpdateUser mutation
class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, id, username=None, email=None):
        user = User.query.get(id)
        if not user:
            raise Exception("User not found")

        if username:
            user.username = username
        if email:
            user.email = email

        db.session.commit()
        return UpdateUser(user=user)

# Define the DeleteUser mutation
class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        user = User.query.get(id)
        if not user:
            raise Exception("User not found")

        db.session.delete(user)
        db.session.commit()
        return DeleteUser(success=True)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)