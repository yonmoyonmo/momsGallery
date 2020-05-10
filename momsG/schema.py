import graphene
import gallery.schema


class Query(gallery.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
