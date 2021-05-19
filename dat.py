import os.path

class character:
    def __init__(self, path : str = None, name : str = None):

        self.path = path
        self.name = name
        self.description = read_description(self.path)
        self.prim_img = None
        self.sec_img = None
        if os.path.isfile(f"{path}/{path}_1.png"):
            self.prim_img = f"{path}/{path}_1.png"


        if os.path.isfile(f"{path}/{path}_2.png"):
            self.sec_img = f"{path}/{path}_2.png"
        




    def __str__(self):
        return self.name
    def __eq__(self, value):
        if type(value) == character:
            return self.name == value.name
        elif type(value) == str:
            return self.name == value
        

def read_description(path):
    with open(path + "/description.txt","r", encoding="UTF-8") as f:
        lines = f.read()


    return lines
