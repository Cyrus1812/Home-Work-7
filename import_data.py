def import_data():
        with open('Phonebookt.txt', 'r',encoding="utf=8") as file:
            txt = set(file.read().split("\n"))
            print(txt)
