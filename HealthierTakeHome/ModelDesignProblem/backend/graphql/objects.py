import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import desc


from ..models import Provider as ProviderModel, \
    Client as ClientModel, \
    JournalEntry as JournalModel, \
    Plan as PlanModel, \
    ClientProvider as ClientProviderModel


class ProviderObject(SQLAlchemyObjectType):
    provider_id = graphene.Int(source='id')

    class Meta:
        model = ProviderModel
        interfaces = (relay.Node, )


class ClientObject(SQLAlchemyObjectType):
    client_id = graphene.Int(source='id')

    class Meta:
        model = ClientModel
        interfaces = (relay.Node, )

    journal_entries = graphene.List(
        lambda: JournalObject, 
        entry=graphene.String(), date_entered=graphene.DateTime() 
        )

    def resolve_journal_entries(self, info):
        query = JournalObject.get_query(info=info)
        query = query.filter(JournalModel.user_id == self.id)
        query.order_by(desc(JournalModel.date_entered))

        return query.all()

class PlanObject(SQLAlchemyObjectType):
    provider_id = graphene.Int(source='id')

    class Meta:
        model = PlanModel
        interfaces = (relay.Node, )


class ClientProviderObject(SQLAlchemyObjectType):
    provider_id = graphene.Int(source='id')

    class Meta:
        model = ClientProviderModel
        interfaces = (relay.Node, )



class JournalObject(SQLAlchemyObjectType):

     class Meta:
        model = JournalModel
        interfaces = (relay.Node, )


class JournalInput(graphene.InputObjectType):
    entry = graphene.String()