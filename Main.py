from os.path import exists
from CSV_creating import creating
from File_writing import writing_scv
from File_writing import writing_txt
from import_data import import_data


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()
get_phonebook = input("Показать заполненную телефонную книгу y/n? ")
if get_phonebook == "y":
    print(import_data())



writing_scv()
writing_txt()