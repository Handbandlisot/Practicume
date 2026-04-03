def arrange(string):
    '''
    Concutinate string and sort it's letters
    '''
    string_list = list(string)
    sorted_string_list = sorted(string_list)
    return ''.join(sorted_string_list)


sentence = input()
print(arrange(sentence))
