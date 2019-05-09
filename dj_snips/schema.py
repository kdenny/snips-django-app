# from graphene import ObjectType, Node, Schema, List, String, Int, Field
import graphene
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import FeatureContent, ProductContent
from querybot import schema

class Query(challenge.schema.game.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)

# class FeatureNode(DjangoObjectType):
#     class Meta:
#         model = FeatureContent
#
#
# class ProductNode(DjangoObjectType):
#
#     class Meta:
#         model = ProductContent
#
#
# class Query(graphene.ObjectType):
#     feature = graphene.Field(FeatureNode, contentful_id=graphene.String(), title=graphene.String())
#     features = graphene.List(FeatureNode, product_id=graphene.String(), product_title=graphene.String())
#
#     product = graphene.Field(ProductNode, contentful_id=graphene.String(), title=graphene.String())
#     products = graphene.List(ProductNode)
#
#     def resolve_feature(self, info, **kwargs):
#         contentful_id = kwargs.get('contentful_id')
#         title = kwargs.get('title')
#
#         if contentful_id is not None:
#             return FeatureContent.objects.get(contentful_id=contentful_id)
#         if title is not None:
#             return FeatureContent.objects.filter(title__iexact=title)[0]
#         return None
#
#
#     def resolve_product(self, info, **kwargs):
#         contentful_id = kwargs.get('contentful_id')
#         title = kwargs.get('title')
#
#         if contentful_id is not None:
#             return ProductContent.objects.get(contentful_id=contentful_id)
#         if title is not None:
#             return ProductContent.objects.filter(title__iexact=title)[0]
#         return None
#
#
#     def resolve_features(self, info, **kwargs):
#         product_id = kwargs.get('product_id')
#         product_title = kwargs.get('product_title')
#
#         if product_id is not None:
#             return FeatureContent.objects.filter(product__contentful_id=product_id)
#         elif product_title is not None:
#             return FeatureContent.objects.filter(product__title__iexact=product_title)
#         else:
#             return FeatureContent.objects.all()
#
#     def resolve_products(self, info, **kwargs):
#         return ProductContent.objects.all()


schema = graphene.Schema(query=Query)
