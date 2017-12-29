from parser import get_parsed

captions = get_parsed()

pos = []
neg = []

for x in captions:
    for elem in x:
        if elem[1] == 0:
            pos.append(elem[2] + " .\n")
        else:
            neg.append(elem[2] + " .\n")

pos_f = open("rt-polarity.pos","w")
neg_f = open("rt-polarity.neg","w")

for elem in pos:
    pos_f.writelines(elem)

for elem in neg:
    neg_f.writelines(elem)


pos_f.close()
neg_f.close()
