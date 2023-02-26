import re
import numpy as np
from collections import defaultdict
from .interfaces import CorpusParser
from ..tokenizers.services import TokenizerService

class MedlineParser(CorpusParser):
    def __init__(self, config, tokenizer_service: TokenizerService) -> None:
        super().__init__(config, tokenizer_service)

    def get_data(self, PATH_TO_FILE):
        ID_marker = re.compile('\.I.')
        with open(PATH_TO_FILE, 'r') as f:
            text = f.read().replace('\n', " ")
            lines = re.split(ID_marker, text)
            lines.pop(0)
        return lines

    def get_txt_data(self):
        txt_list = self.get_data(self.docs_path)
        chunk_start = re.compile('\.[W]')
        txt_data = defaultdict(dict)
        for line in txt_list:
            entries = re.split(chunk_start, line)
            id = entries[0].strip()
            text = entries[1]
            txt_data[id]['text'] = text
            txt_data[id]['tokens'] = self._tokenizer.tokenize(text)
        return txt_data

    def get_qry_data(self):
        qry_list = self.get_data(self.qry_path)
        chunk_start = re.compile('\.[W]')
        qry_data = defaultdict(dict)
        for n in range(0, len(qry_list)-1):
            line = qry_list[n+1]
            _, question = re.split(chunk_start, line)
            qry_data[n+1]['question'] = question
            qry_data[n+1]['tokens'] = self._tokenizer.tokenize(question)
        return qry_data

    def get_rel(self):
        med_rel = defaultdict(list)

        with open(self.rel_path, 'r') as f:
            for line in f:
                line = re.split(' ', line)
                med_rel[int(line[0])].append(int(line[2]))

        return med_rel

    def get_rel_numpy(self):
        med_rel_data = open(self.rel_path)
        med_np = np.loadtxt(med_rel_data, dtype=int)

        med_rel_rat = defaultdict(list)
        for row in med_np:
            med_rel_rat[row[0]].append(tuple(row[2:]))
        med_rel_data.close()
        return med_rel_rat
