import sys
from parser import get_parsed, get_raw_parsed


captions = get_parsed()

pos = []
neg = []


raw_cap = get_raw_parsed()

for filename, elem in raw_cap:
    output_f = open("parsed_captions/" + filename, 'w')

    for ll in elem:
        output_f.writelines(ll + "\n")

print("FINISHED")
sys.exit(0)

for x in captions:
    for elem in x:
        if elem[1] == 0:
            neg.append(elem[2] + " .\n")
        else:
            pos.append(elem[2] + " .\n")

pos_f = open("rt-polarity.pos","w")
neg_f = open("rt-polarity.neg","w")

for elem in pos:
    pos_f.writelines(elem)

for elem in neg:
    neg_f.writelines(elem)


pos_f.close()
neg_f.close()
