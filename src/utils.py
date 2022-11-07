import os
from collections import defaultdict
import re

def filenamesFromPath(path = "documents"):
    filenames = os.listdir(path)
    return filenames

def wordsFrequencyInText(text:str):
    PATTERN = '\w+'
    counts = defaultdict(int)
    for word in re.findall(PATTERN, text):
        counts[word] += 1
    return counts

def wordsFrequencyInPath(path:str):
    filenames = filenamesFromPath(path)
    results = defaultdict(int)

    for filename in filenames:
        filenamePath = f'{path}/{filename}'
        wordsFrequency = wordsFrequencyInFileFromPath(filenamePath) 

        for key,value in wordsFrequency.items():
            if results[key]:
                results[key] += value
            else:
                results[key] = value

    return results

def wordsFrequencyInFileFromPath(path):
    with open(path) as f:
        text = f.read()
        return wordsFrequencyInText(text)



