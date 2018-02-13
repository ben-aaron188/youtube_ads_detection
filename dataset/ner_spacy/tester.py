from __future__ import division
from utils import *
from tags import *
from extractor import *

text = "My husband and I stayed at the Hyatt Regency while attending a family wedding in Chicago. From the moment we entered the beautiful lobby we were treated as if we were returning friends. Our rooms were ready upon arrival, and they were just as impressive as when I viewed them online. The location couldn't be more convenient to access all of Chicago's shopping and dining areas. We dined in Seston's Chop House, which I highly recommend. The staff at the hotel are professionals who work to make your stay there a grand experience. The Hyatt Regency Chicago is the only place we will stay when we return to the Windy City!"


parsed_input = parse_input(text)

pos_ner_extract(parsed_input, 'bogusname', True)