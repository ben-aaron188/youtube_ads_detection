import os, csv, sys

class Dataprovider:


    def __init__(self):
        self.collect_data()


    def get_filename_to_index_mapping(self):
        mapping = {}

        with open('parsed_captions/mapping.txt', 'r') as f:
            data = f.readlines()

            for elem in data:
                split = elem.split("<||>")
                mapping[split[1].replace("\n", "")] = split[0]

        return mapping


    def get_parsed(self):
        captions = {}

        for filename in os.listdir("parsed_captions"):
                if filename != ".DS_Store" and filename != 'raw_titles':
                    with open("parsed_captions/" + filename) as f:
                        captions[filename.replace(".txt", "")] = f.readlines()

        return captions


    def collect_data(self):

        # This is the raw csv output
        self._raw_csv  = []

        # Dictionary with index of video to title of video
        self._i_to_title = {}

        # Dictionary with title of video to index of video
        self._title_to_i = {}

        # Dictionary with index of video to content of video
        self._i_to_content = {}

        # Dictionary with index of video to polarity (1=pos, 0=neg)
        self._i_to_pol = {}

        # Dictionary with index of video to indices of positive sequences
        self._i_to_i_pos = {}

        # Dictionary with index of video to indices of negative sequences
        self._i_to_i_neg = {}

        # Dictionary with index of video to positive sequences
        self._i_to_content_pos = {}

        # Dictionary with index of video to negative sequences
        self._i_to_content_neg = {}

        # Number of sequences
        self._num_sequences = 0

        # Number of positive sequences
        self._num_positive = 0

        # Number of negative sequences
        self._num_negative = 0

        # Vocab of all captions
        self._vocab = []

        # Vocab size
        self._vocab_size = []

        parsed_captions = self.get_parsed()
        self._title_to_i = self.get_filename_to_index_mapping()

        with open('segment_labeling.txt', 'r') as txtf:
            data_raw = list(txtf.readlines())
            data = []

            for string in data_raw:
                title = [string[:(string.find('.txt') + 4)]]
                rest = string[(string.find('.txt') + 4):].split(",")
                rest = [x.replace("\n", "") for x in rest[1:] if x != '']

                # Decrement index since we start 0 and the files start at 1
                rest = [(int(x)-1) for x in rest if x != '']

                data.append(title + rest)

            for elem in data:
                title = elem[0].replace("\ufeff", "")
                index = self._title_to_i[title]

                self._raw_csv.append(elem)
                self._i_to_title[index] = title

                if title[:3] == 'yes':
                    self._i_to_pol[index] = 1
                else:
                    self._i_to_pol[index] = 0

                content = parsed_captions[index]
                all_ind = list(range(len(content)))
                pos_ind = elem[1:]
                neg_ind = list(set(all_ind) - set(pos_ind))

                for row in content:
                    self._vocab += row.split(" ")

                self._num_sequences += len(all_ind)
                self._num_positive += len(pos_ind)
                self._num_negative += len(neg_ind)
                self._i_to_content[index] = content
                self._i_to_i_pos[index] = pos_ind
                self._i_to_i_neg[index] = neg_ind
                self._i_to_content_pos[index] = [content[x] for x in pos_ind]
                self._i_to_content_neg[index] = [content[x] for x in neg_ind]

        self._vocab = set(self._vocab)
        self._vocab_size = len(self._vocab)


    def write_content_to_file(self):

        for key, value in self._i_to_content_pos.items():
            pos = open("separated/pos/" + key + ".txt","w")
            pos.writelines(value)
            pos.close()

        for key, value in self._i_to_content_neg.items():
            neg = open("separated/neg/" + key + ".txt","w")
            neg.writelines(value)
            neg.close()


    @property
    def raw_csv(self):
        return self._raw_csv

    @property
    def i_to_title(self):
        return self._i_to_title

    @property
    def title_to_i(self):
        return self._title_to_i

    @property
    def i_to_content(self):
        return self._i_to_content

    @property
    def num_sequences(self):
        return self._num_sequences

    @property
    def num_positive(self):
        return self._num_positive

    @property
    def num_negative(self):
        return self._num_negative

    @property
    def vocab(self):
        return self._vocab

    @property
    def vocab_size(self):
        return self._vocab_size

    @property
    def i_to_pol(self):
        return self._i_to_pol

    @property
    def i_to_i_pos(self):
        return self._i_to_i_pos

    @property
    def i_to_i_neg(self):
        return self._i_to_i_neg

    @property
    def i_to_content_pos(self):
        return self._i_to_content_pos

    @property
    def i_to_content_neg(self):
        return self._i_to_content_neg
