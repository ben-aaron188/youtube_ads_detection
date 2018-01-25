import sys, os


def get_raw_parsed():
    parsed_captions = []
    raw_captions = []

    for filename in os.listdir("../output_dir"):
        raw = []

        if filename != ".DS_Store":
            with open("../output_dir/" + filename) as f:

                for elem in f.readlines():
                    if "-->" not in elem:

                        elem = elem.replace("\n", "")

                        while ">" in elem:
                            rub = elem[elem.index("<"):elem.index(">")+1]
                            elem = elem.replace(rub, "")

                        while "[" in elem:
                            rub = elem[elem.index("["):elem.index("]")+1]
                            elem = elem.replace(rub, "")


                        if elem != "" and not elem.isdigit():
                            raw.append(elem)


        raw_captions.append([filename, raw])

    return raw_captions


def get_parsed():
    captions = []

    for filename in os.listdir("../output_dir"):
        if filename != ".DS_Store":

            with open("../output_dir/" + filename) as f:
                if filename[:2] == "no":
                    captions.append([0,f.readlines()])
                else:
                    captions.append([1, f.readlines()])

    filtered = []
    count = 0

    for pol, caption in captions:
        filt = []

        for elem in caption:
            if "-->" not in elem:

                elem = elem.replace("\n", "")

                while ">" in elem:
                    rub = elem[elem.index("<"):elem.index(">")+1]
                    elem = elem.replace(rub, "")

                while "[" in elem:
                    rub = elem[elem.index("["):elem.index("]")+1]
                    elem = elem.replace(rub, "")


                if elem != "" and not elem.isdigit():
                    count += 1
                    filt.append([count, pol, elem])

        filtered.append(filt)

    return filtered
