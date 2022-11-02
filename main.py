from src.utils import get_all_file_names, get_all_words_frequency, get_words_frequency


text = "Hello World friend, World"

# a = get_all_file_names('docs')
# b = get_words_frequency(text)
c = get_all_words_frequency('docs')
for key, value in c.items():
    print(key, value)


# print(a)
# print(b)
# print(c)
