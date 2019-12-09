from pycrfsuite import Tagger
import os
from crf_predict.models import Doc, Ent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 'CRF')
MODEL_DIR = os.path.join(MODEL_DIR, 'tmp.model')

tagger = Tagger()
tagger.open(MODEL_DIR)

from train_crf import train

def predict_ents(test_docs):
    entity_dict = {}

    for doc in test_docs:
        tokens = []
        pos_tags = []
        for sent in doc.sents:
            for token in sent:
                tokens.append(str(token))
                pos_tags.append(token.tag_)

        features = train.feature_extractor.extract(tokens, pos_tags)
        labels = tagger.tag(features)

        entities = train.decode_bilou(labels, doc.sents, doc)
        doc.ents = entities

        for ent in entities:
            if ent.label_ not in entity_dict:
                entity_dict[ent.label_] = set([ent.text])
            else:
                entity_dict[ent.label_].add(ent.text)

    return entity_dict, test_docs




