import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from sqlalchemy import desc

from ..models import Wombat as WombatModel
from ..graphql.objects import WombatObject


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    wombats = graphene.List(
        lambda: WombatObject,
        name=graphene.String(),
        dob=graphene.Date(),
        descend=graphene.Boolean(),
        ascend=graphene.Boolean())

    def resolve_wombats(self, info, name=None, dob=None, descend=True, ascend=False):
        query = WombatObject.get_query(info)

        if name:
            query = query.filter(WombatModel.name == name)
            return query

        if ascend:
            query = query.order_by(WombatModel.dob)
            descend = False

        if descend:
            query = query.order_by(desc(WombatModel.dob))

        return query.all()

    all_wombats = SQLAlchemyConnectionField(WombatObject.connection)
