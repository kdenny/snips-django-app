from django.shortcuts import render
from .models import Entity, EntityRecord, EntitySlot, Intent, Utterance, Synonym
from .write_yaml import write_yaml, make_nlu_model_json, make_nlu_model_yaml, write_json
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from snips_nlu import SnipsNLUEngine
from snips_nlu.dataset import Dataset
from snips_nlu.default_configs import CONFIG_EN
from pprint import pprint


# Create your views here.

dataset = Dataset.from_yaml_files("en", ["data.yaml"])
j = dataset.json
m = json.dumps(j)
sample_dataset = json.loads(m)



nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
nlu_engine = nlu_engine.fit(sample_dataset, force_retrain=False)

class MakeYAMLFromDB(APIView):
    def get(self, request):
        global nlu_engine
        d = request.data
        el = []
        entities = list(Entity.objects.all().values('name', 'automatically_extensible', 'use_synonyms', 'matching_strictness'))
        for e in entities:
            jm = e
            jm['type'] = 'entity'
            lll = list(EntityRecord.objects.filter(entity__name=e['name']).values_list('word', flat=True))
            vals_list = []
            for v in lll:
                se = list(Synonym.objects.filter(entity_record__word=v).values_list('word', flat=True))
                iw = se
                if len(iw) > 0:
                    iw.append(v)
                    istring = ", ".join(iw)
                    iistring = '[' + istring + ']'
                    vals_list.append(iistring)
                else:
                    vals_list.append(v)


            jm['values'] = vals_list
            el.append(jm)

        il = []
        intents = list(Intent.objects.all().values('name'))
        for i in intents:
            uu = i
            uu['type'] = 'intent'
            utts = list(Utterance.objects.filter(intent__name=i['name']).values_list('text', flat=True))
            uu['utterances'] = utts
            sl = list(EntitySlot.objects.filter(intent__name=i['name']).values('name', 'entity__name'))
            slots = []
            for s in sl:
                uj = {
                    'name': s['name'],
                    'entity': s['entity__name']
                }
                slots.append(uj)
            uu['slots'] = slots
            il.append(uu)

        yaml_data = il + el

        d = write_yaml(yaml_data)
        ui = nlu_engine
        ym = make_nlu_model_yaml(ui)
        nlu_engine = ym
        data = {
            'data': d
        }

        return Response(data)

class MakeJSONFromDB(APIView):
    def get(self, request):
        d = request.data
        el = {}

        entities = list(Entity.objects.all().values('name', 'automatically_extensible', 'use_synonyms', 'matching_strictness'))
        for e in entities:
            jm = e
            jm['type'] = 'entity'
            lll = list(EntityRecord.objects.filter(entity__name=e['name']).values_list('word', flat=True))
            vals_list = []
            for v in lll:
                se = list(Synonym.objects.filter(entity_record__word=v).values_list('word', flat=True))
                iw = se
                if len(iw) > 0:
                    iw.append(v)
                    istring = ", ".join(iw)
                    iistring = '[' + istring + ']'
                    vals_list.append(iistring)
                else:
                    vals_list.append(v)

            jm['values'] = vals_list
            el[e['name']] = jm


        il = {}
        intents = list(Intent.objects.all().values('name'))
        for i in intents:
            uu = i
            uu['type'] = 'intent'
            utts = list(Utterance.objects.filter(intent__name=i['name']).values_list('text', flat=True))
            uu['utterances'] = utts
            sl = list(EntitySlot.objects.filter(intent__name=i['name']).values('name', 'entity__name'))
            slots = []
            for s in sl:
                uj = {
                    'name': s['name'],
                    'entity': s['entity__name']
                }
                slots.append(uj)
            uu['slots'] = slots
            il[uu['name']] = uu

        yd = {
            'entities': el,
            'intents': il,
            'language': 'en'
        }

        d = write_json(yd)
        # make_nlu_model_yaml('data.yaml', nlu_engine)
        data = {
            'data': d
        }

        return Response(data)


class CommandsParse(APIView):
    def post(self, request):
        m = request.data
        msg = m['msg']
        res = nlu_engine.parse(msg)
        pprint(res)


        return Response(res)