import re
import numpy as np
from collections import defaultdict
from .interfaces import CorpusParser
from ..tokenizers.services import TokenizerService

class CisiParser(CorpusParser):
    def __init__(self, config, tokenizer_service: TokenizerService) -> None:
        super().__init__(config, tokenizer_service)

    def get_data(self, PATH_TO_FILE):
        ID_marker = re.compile('\.I\s')
        with open(PATH_TO_FILE, 'r') as f:
            text = f.read().replace('\n', " ")
            lines = re.split(ID_marker, text)
            lines.pop(0)
        return lines

    def get_txt_data(self):
        txt_list = self.get_data(self.docs_path)
        chunk_start = re.compile('\.[T,A,W,X]')
        txt_data = defaultdict(dict)
        for line in txt_list:
            entries = re.split(chunk_start, line)
            id = int(entries[0].strip())
            title = entries[1]
            author = entries[2]
            text = entries[3]
            cross_references = entries[4]

            txt_data[id]['title'] = title
            txt_data[id]['author'] = author
            txt_data[id]['text'] = text
            txt_data[id]['tokens'] = self._tokenizer.tokenize(text)
            txt_data[id]['cross_references'] = cross_references

        return txt_data

    def get_qry_data(self):
        qry_list = self.get_data(self.qry_path)
        chunk_start = re.compile('\.[W]')
        qry_data = defaultdict(dict)
        for n in range(len(qry_list)):
            line = qry_list[n]
            _, question = re.split(chunk_start, line)
            qry_data[n+1]['question'] = question
            qry_data[n+1]['tokens'] = self._tokenizer.tokenize(question)
        return qry_data

    def get_rel(self):
        cisi_rel = defaultdict(list)

        with open(self.rel_path, 'r') as f:
            for line in f:
                line = re.findall(r"\d+\.\d+| \d+", line)
                cisi_rel[int(line[0])].append(int(line[1]))
        return cisi_rel

    def get_rel_numpy(self):
        cisi_rel_data = open(self.rel_path)
        cisi_np = np.loadtxt(cisi_rel_data, dtype=int)

        cisi_rel_rat = defaultdict(list)
        for row in cisi_np:
            cisi_rel_rat[row[0]].append(tuple(row[1:]))
        cisi_rel_data.close()
        return cisi_rel_rat
