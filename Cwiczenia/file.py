 #Zadanie 8

class Filemanager:
    def __init__(self,file_name):
        self.file_name = file_name
    def read_file(self):
        f = open(f'{self.file_name}', "r")
        print(f.read())
    def update_file(self, text_data):
        f = open(f'{self.file_name}', 'w')
        f.write(text_data)