# student_dict = {
    # "student": ["Angela", "James", "Lily"], 
    # "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
    # #Access key and value
    # pass

# from numpy import prod
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # #Access index and row
    # #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO: 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas
nato_phonetic_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
words_data_frame = pandas.DataFrame(nato_phonetic_alphabet)

phonetic_dict = {row.letter: row.code for (index, row) in words_data_frame.iterrows()}
# print(phonetic_dict)

#TODO: 2   Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word to create phonetic code: ").upper()

phonetic_code = [phonetic_dict[letter] for letter in word]

print(phonetic_code)

#NOTE: review list comprehension
