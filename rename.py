import os
class cambiar : 
    def __init__(self, path, name) :
        self._path = path
        self._name = name

    def cambiarArch(self):
        try :
            for lago in os.listdir(self._path) :
                rename = self._name + lago
                os.rename(self._path + lago, self._path + rename)
                print("Exito")
        except :
            print("Error")
test = cambiar("C:/Users/userpc/folder/filestorename/", "here-text")
test.cambiarArch()