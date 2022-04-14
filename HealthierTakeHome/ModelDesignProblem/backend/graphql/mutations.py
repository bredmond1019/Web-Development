import graphene
from datetime import date

from backend import db
# from ..graphql.objects import WombatObject
# from ..models import Wombat as WombatModel


# class WombatMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#         dob = graphene.Date(required=True)

#     wombat = graphene.Field(lambda: WombatObject)

#     def mutate(self, info, name, dob):
#         wombat = WombatModel(name=name, dob=dob)

#         db.session.add(wombat)
#         db.session.commit()

#         return WombatMutation(wombat=wombat)


# class Mutation(graphene.ObjectType):
#     mutate_wombat = WombatMutation.Field()
