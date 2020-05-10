import graphene
from graphene_django.types import DjangoObjectType
from gallery.models import Photo, Comment


class PhotoType(DjangoObjectType):
    class Meta:
        model = Photo


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query(object):
    all_photos = graphene.List(PhotoType)
    all_comments = graphene.List(CommentType)

    def resolve_all_photos(self, info, **kwargs):
        return Photo.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.select_related('post').all()
