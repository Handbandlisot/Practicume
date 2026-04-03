import string


sentence = input()

translator = str.maketrans('', '', string.punctuation)
clean_sentence = sentence.translate(translator)
words_list = clean_sentence.split()

print(set(words_list))
