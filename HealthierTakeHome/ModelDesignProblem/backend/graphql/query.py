import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from sqlalchemy import desc

from ..models import Provider as ProviderModel, \
    Client as ClientModel, \
    JournalEntry as JournalModel, \
    Plan as PlanModel, \
    ClientProvider as ClientProviderModel

from ..graphql.objects import ProviderObject, ClientObject, JournalObject



class Query(graphene.ObjectType):
    node = relay.Node.Field()

    providers = graphene.List(lambda: ProviderObject, email=graphene.String(), provider_id=graphene.Int())
    clients = graphene.List(lambda: ClientObject, email=graphene.String(), client_id=graphene.Int())


    def resolve_providers(self, info, email=None):
        query = ProviderObject.get_query(info)

        if email:
            query = query.filter(ProviderModel.email == email)
        
        return query.all()


    def resolve_clients(self, info, email=None):
        query = ClientObject.get_query(info)

        if email:
            query = query.filter(ClientModel.email == email)
        
        return query.all()



    all_providers = SQLAlchemyConnectionField(ProviderObject.connection)
    all_clients = SQLAlchemyConnectionField(ClientObject.connection)








    # wombats = graphene.List(
    #     lambda: WombatObject,
    #     name=graphene.String(),
    #     dob=graphene.Date(),
    #     descend=graphene.Boolean(),
    #     ascend=graphene.Boolean())

    # def resolve_wombats(self, info, name=None, dob=None, descend=True, ascend=False):
    #     query = WombatObject.get_query(info)

    #     if name:
    #         query = query.filter(WombatModel.name == name)
    #         return query

    #     if ascend:
    #         query = query.order_by(WombatModel.dob)
    #         descend = False

    #     if descend:
    #         query = query.order_by(desc(WombatModel.dob))

    #     return query.all()

    # all_wombats = SQLAlchemyConnectionField(WombatObject.connection)
