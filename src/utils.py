import os
from collections import defaultdict
import re

def get_all_file_names(path = "documents"):
    filenames = os.listdir(path)
    return filenames

def get_words_frequency(text:str):
    counts = defaultdict(int)
    for word in re.findall('\w+', text):
        counts[word] += 1
    return counts

def get_all_words_frequency(path:str):
    filenames = get_all_file_names(path)
    results = defaultdict(int)
    for filename in filenames:
        with open(f"{path}/{filename}") as f:
            counts = get_words_frequency(f.read())
            for key,value in counts.items():
                if results[key] is not None:
                    results[key] += value
                else:
                    results[key] = value
    return results


