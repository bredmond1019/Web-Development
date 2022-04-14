import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


from ..models import \
    Provider as ProviderModel, \
    Client as ClientModel, \
    JournalEntry as JournalModel


class ProviderObject(SQLAlchemyObjectType):

    class Meta:
        model = ProviderModel
        interfaces = (relay.Node, )


class ClientObject(SQLAlchemyObjectType):

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
        query.order_by(JournalModel.date_entered)

        return query.all()



class JournalObject(SQLAlchemyObjectType):

     class Meta:
        model = JournalModel
        interfaces = (relay.Node, )


class JournalInput(graphene.InputObjectType):
    entry = graphene.String()