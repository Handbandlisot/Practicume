def vow_and_con(text):
    vowels = ['а', 'е', 'ё', 'и', 'о',
              'у', 'ы', 'э', 'ю', 'я']
    consonants = ['б', 'в', 'г', 'д', 'ж',
                  'з', 'й', 'к', 'л', 'м',
                  'н', 'п', 'р', 'с', 'т',
                  'ф', 'х', 'ц', 'ч', 'ш', 'щ'
                  ]
    vowels_count = 0
    consonants_count = 0
    for letter in vowels:
        vowels_count += text.count(letter)
    print(vowels_count)
    for letter in consonants:
        consonants_count += text.count(letter)
    print(consonants_count)
    

text = 'Представьте, что здесь некий осмысленный текст на русском'
vow_and_con(text)
