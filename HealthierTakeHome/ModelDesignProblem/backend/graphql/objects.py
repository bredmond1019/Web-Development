import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Wombat as WombatModel


class WombatObject(SQLAlchemyObjectType):

    class Meta:
        model = WombatModel
        interfaces = (relay.Node, )
