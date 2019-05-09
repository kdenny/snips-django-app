import yaml
import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.dataset import Dataset
from snips_nlu.default_configs import CONFIG_EN
from pprint import pprint

def write_yaml(data):

    with open('data.yaml', 'w') as outfile:
        t = '# Name \n---\n'
        for i, o in enumerate(data):
            a = yaml.dump(o)
            t += a
            if i != (len(data) - 1):
                t += '---\n'

        outfile.write(t)

    # stream = open('data.yaml', 'r')
    # a = yaml.load_all(stream)

    dataset_yaml = io.StringIO('''{0}'''.format(t))

    return dataset_yaml

def write_json(data):

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    return data


def make_nlu_model_json(fname):
    docs = yaml.load_all(stream)
    ll = []
    for doc in docs:
        i = {}
        for k, v in doc.items():
            i[k] = v
        ll.append(i)

    dataset = Dataset.from_yaml_files("en", [ll])

    nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
    nlu_engine = nlu_engine.fit(dataset)
    text = "Please turn the light on in the kitchen"
    parsing = nlu_engine.parse(text)


def make_nlu_model_yaml(nlu_engine):
    dataset = Dataset.from_yaml_files("en", ["data.yaml"])
    j = dataset.json
    m = json.dumps(j)
    sample_dataset = json.loads(m)
    nlu_engine = nlu_engine.fit(sample_dataset, force_retrain=True)

    return nlu_engine

