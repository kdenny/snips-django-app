# from graphene import ObjectType, Node, Schema, List, String, Int, Field
import graphene
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from .models import Entity, EntityRecord, EntitySlot, Synonym, Intent, Utterance

class EntityNode(DjangoObjectType):
    class Meta:
        model = Entity

class EntityRecordNode(DjangoObjectType):
    class Meta:
        model = EntityRecord

class EntitySlotNode(DjangoObjectType):
    class Meta:
        model = EntitySlot

class SynonymNode(DjangoObjectType):
    class Meta:
        model = Synonym

class IntentNode(DjangoObjectType):
    class Meta:
        model = Intent

class UtteranceNode(DjangoObjectType):
    class Meta:
        model = Utterance




class Query(graphene.ObjectType):
    entity_records = graphene.List(EntityRecordNode, entity_name=graphene.String(), entity_slot_id=graphene.String())
    entity_slots = graphene.List(EntitySlotNode, entity_name=graphene.String(), intent=graphene.String())
    synonyms = graphene.List(SynonymNode, entity_record=graphene.String())
    utterances = graphene.List(UtteranceNode, intent=graphene.String())

    entities = graphene.List(EntityNode)
    intents = graphene.List(IntentNode)

    entity = graphene.Field(EntityNode, name=graphene.String())
    intent = graphene.Field(IntentNode, name=graphene.String())

    def resolve_entities(self, info, **kwargs):
        return Entity.objects.all()

    def resolve_intents(self, info, **kwargs):
        return Intent.objects.all()

    def resolve_intent(self, info, **kwargs):
        name = kwargs.get('name')

        if name is not None:
            return Intent.objects.get(name=name)
        return None

    def resolve_entity(self, info, **kwargs):
        name = kwargs.get('name')

        if name is not None:
            return Entity.objects.get(name=name)
        return None

    def resolve_entity_records(self, info, **kwargs):
        entity_name = kwargs.get('entity_name')
        entity_slot_id = kwargs.get('entity_slot_id')

        if entity_name is not None:
            return EntityRecord.objects.filter(entity__name=entity_name)
        if entity_slot_id is not None:
            return EntityRecord.objects.filter(entity__intent_slots__id=entity_slot_id)
        return None

    def resolve_entity_slots(self, info, **kwargs):
        entity_name = kwargs.get('entity_name')
        intent = kwargs.get('intent')

        if entity_name is not None:
            return EntitySlot.objects.filter(entity__name=entity_name)
        if intent is not None:
            return EntitySlot.objects.filter(intent__name=intent)
        return None

    def resolve_utterances(self, info, **kwargs):
        intent = kwargs.get('intent')

        if name is not None:
            return Utterance.objects.filter(intent__name=intent)
        else:
            return Utterance.objects.all()

    def resolve_synonyms(self, info, **kwargs):
        entity_record = kwargs.get('entity_record')

        if entity_record is not None:
            return Synonym.objects.filter(entity_record__name=entity_record)
        else:
            return None



schema = graphene.Schema(query=Query)
