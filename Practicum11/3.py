import string


sentence = input("Введите предложение: ")

translator = str.maketrans('', '', string.punctuation)
clean_sentence = sentence.translate(translator)
words_list = clean_sentence.split()

print(words_list)
