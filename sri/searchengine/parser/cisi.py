import re
import numpy as np
from collections import defaultdict


def get_data(PATH_TO_FILE):
    ID_marker = re.compile('\.I\s')
    with open(PATH_TO_FILE, 'r') as f:
        text = f.read().replace('\n', " ")
        lines = re.split(ID_marker, text)
        lines.pop(0)
    return lines


def get_txt_data(txt_list: list[str]):
    chunk_start = re.compile('\.[T,A,W,X]')
    txt_data = defaultdict(dict)
    for line in txt_list:
        entries = re.split(chunk_start, line)
        id = entries[0].strip()
        title = entries[1]
        author = entries[2]
        text = entries[3]
        cross_references = entries[4]
        
        txt_data[id]['title'] = title
        txt_data[id]['author'] = author
        txt_data[id]['text'] = text
        txt_data[id]['cross_references'] = cross_references
        
    return txt_data


def get_qry_data(qry_list: list[str]):
    chunk_start = re.compile('\.[W]')
    qry_data = defaultdict(dict)
    for n in range(0, len(qry_list)-1):
        line = qry_list[n+1]
        _, question = re.split(chunk_start, line)
        qry_data[n+1]['question'] = question
    return qry_data


def get_rel(PATH_TO_CISI_REL: str):
    cisi_rel = defaultdict(list)

    with open(PATH_TO_CISI_REL, 'r') as f:
        for line in f:
            line = re.findall(r"\d+\.\d+| \d+", line)
            cisi_rel[int(line[0])].append(line[1])
    return cisi_rel


def get_rel_numpy(PATH_TO_CISI_REL: str):
    cisi_rel_data = open(PATH_TO_CISI_REL)
    cisi_np = np.loadtxt(cisi_rel_data, dtype=int)

    cisi_rel_rat = defaultdict(list)
    for row in cisi_np:
        cisi_rel_rat[row[0]].append(tuple(row[1:]))
    return cisi_rel_rat