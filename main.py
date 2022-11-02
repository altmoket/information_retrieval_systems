from src.utils import get_all_file_names, get_words_frequency


text = "Hello World friend, World"

a = get_all_file_names('documents')
b = get_words_frequency(text)

print(a)
print(b)
