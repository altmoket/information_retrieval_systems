import os

def get_all_file_names():
    filenames = os.listdir('documents')
    return filenames

a = get_all_file_names()
print(a)
