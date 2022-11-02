import os
from collections import defaultdict
import re

def get_all_file_names():
    filenames = os.listdir('documents')
    return filenames

def get_words_frequency(file:str):
    counts = defaultdict(int)
    for word in re.findall('\w+', file):
        counts[word] += 1
    return counts

text = "Hello World friend, World"

a = get_all_file_names()
b = get_words_frequency(text)
print(a)
print(b)
