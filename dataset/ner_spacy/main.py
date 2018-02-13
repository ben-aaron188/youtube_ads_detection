#import dependencies
from __future__ import division
import csv
from utils import *
from extractor import *
from tags import *
import os
import os.path
from pathlib import Path
import glob
import time
import spacy

dirname = os.path.dirname

def main_extractor(input, filename, verbose):
    output_row = [filename]
    if len(input) > 0:
        parsed_input = parse_input(input)
        extraction = pos_ner_extract(parsed_input, filename, verbose)
        for netag in ne_tags:
            ne_freq = count_in_list(extraction, netag)
            output_row.append(ne_freq)
        for postag in pos_tags:
            pos_freq = count_in_list(extraction, postag)
            output_row.append(pos_freq)
        return(output_row)


def analyse_files(filepath, outputappendix, verbose):
    timestr = time.strftime("%d%m%Y%X")
    output_file = []
    tracker = 0
    # take t1
    t1 = time.time()
    for file in Path(filepath).glob('**/*.txt'):
        global filename
        tracker = tracker + 1
        filename = os.path.basename(str(file))
        file_ = open(str(file)).read()
        row = main_extractor(input=file_, filename=filename, verbose=verbose)
        output_file.append(row)
    # take t2
    t2 = time.time()
    # output t2-t1
    elapsed_time = t2 - t1
    print('# secs: ' + str(elapsed_time))
    print('# docs: ' + str(tracker))
    # return output_file
    with open(str(outputappendix) + '_' + timestr + ".csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(output_file)


dir_pos = '../annotated_pos_neg_sequences/indiv_pos'
dir_neg = '../annotated_pos_neg_sequences/indiv_neg'

analyse_files(filepath=dir_pos, outputappendix='pos', verbose=True)

analyse_files(filepath=dir_neg, outputappendix='neg', verbose=True)
