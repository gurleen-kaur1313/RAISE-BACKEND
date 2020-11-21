
import graphene
from graphene.types.argument import Argument
from graphene.types.mutation import Mutation
from graphene_django import DjangoObjectType
from .models import HealthTest, PoliceEmergency, HealthEmergency, Jobs
from graphql import GraphQLError



class TestForHealth(DjangoObjectType):
    class Meta:
        model = HealthTest

class Police(DjangoObjectType):
    class Meta:
        model = PoliceEmergency

class Health(DjangoObjectType):
    class Meta:
        model = HealthEmergency

class jobss(DjangoObjectType):
    class Meta:
        model = Jobs

class Query(graphene.ObjectType):
    getAllTest = graphene.List(TestForHealth)
    getMyTest = graphene.List(TestForHealth)
    police = graphene.List(Police)
    health = graphene.List(Health)
    alljobs = graphene.List(jobss)

    def resolve_getAllTest(self, info):
        return HealthTest.objects.all()

    def resolve_getMyTest(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        return HealthTest.objects.filter(user=active).order_by("-date")

    def resolve_police(self,info):
        return PoliceEmergency.objects.all().order_by("-time")

    def resolve_health(self,info):
        return HealthEmergency.objects.all().order_by("-time")

    def resolve_alljobs(self, info):
        return Jobs.objects.all()


class AddHealthTest(graphene.Mutation):
    myTest = graphene.Field(TestForHealth)

    class Arguments:
        test = graphene.String()
        remarksDoc = graphene.String()
        remarksPat = graphene.String()

    def mutate(self, info, **kwargs):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In!")
        test = HealthTest.objects.create(user=active)
        test.test = kwargs.get("test")
        test.remarksDoc = kwargs.get("remarksDoc")
        test.remarksPat = kwargs.get("remarksPat")

        return AddHealthTest(myTest=test)

class AddPoliceEmergency(graphene.Mutation):
    myEmergency = graphene.Field(Police)

    class Arguments:
        longitude = graphene.Float()
        latitude = graphene.Float()

    def mutate(self, info, **kwargs):
        user = info.context.user
        test = PoliceEmergency.objects.create(user=user)
        test.longitude = kwargs.get("longitude")
        test.latitude = kwargs.get("latitude")

        return AddPoliceEmergency(myEmergency=test)

class AddHealthEmergency(graphene.Mutation):
    myEmergency = graphene.Field(Health)

    class Arguments:
        longitude = graphene.Float()
        latitude = graphene.Float()

    def mutate(self, info, **kwargs):
        user = info.context.user
        test = HealthEmergency.objects.create(user=user)
        test.longitude = kwargs.get("longitude")
        test.latitude = kwargs.get("latitude")

        return AddHealthEmergency(myEmergency=test)

class Mutation(graphene.ObjectType):
    add_test = AddHealthTest.Field()
    add_police = AddPoliceEmergency.Field()
    add_health = AddHealthEmergency.Field()
