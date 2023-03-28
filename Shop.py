from Notebook import*
from NotebookClass import*

class Shop:
    def __init__(self):
        list = []
        self._list = list

    def add_notebook(self,notebook: list):
        self._list.append(notebook)

    def del_notebook(self, notebook: list):
        self._list.remove(notebook)
    
    def print(self):
        for i in self._list:
            print(i)