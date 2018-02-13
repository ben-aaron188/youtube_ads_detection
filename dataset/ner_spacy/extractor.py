#import dependencies
from __future__ import division
from utils import *
from tags import *
import spacy

def pos_ner_extract(main_input, filename, verbose=False):
    extracted_features = []
    print('starting extraction for: ' + filename)
    for sentence in main_input.sents:
        parsed_sent = parse_input(str(sentence))
        for entity in parsed_sent.ents:
            if entity.label_ in ne_tags:
                extracted_features.append(entity.label_)
                if verbose:
                    print('identified ' + str(entity) + ' as ' + entity.label_)
        for token in parsed_sent:
            if token.pos_ in pos_tags:
                extracted_features.append(token.pos_)
                if verbose:
                    print('identified ' + str(token) + ' as ' + token.pos_)
    print('_-_-_-_-_-_-_-_-_-_-_-_-_.')
    return extracted_features
