import graphene
import Profile.schema
import graphql_jwt
import EmergencyServices.schema


class Query(Profile.schema.Query, EmergencyServices.schema.Query, graphene.ObjectType):
    pass


class Mutation(Profile.schema.Mutation,EmergencyServices.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
