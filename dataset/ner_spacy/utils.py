#import dependencies
import os
from spacy.en import English
parser = English()


# function for forcing director
def force_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)


def parse_input(file):
    parsed = parser(file)
    return(parsed)

def count_in_list(input_list, target):
    n = input_list.count(target)
    return n
