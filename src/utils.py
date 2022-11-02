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
