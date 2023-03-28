from Notebook import*
from NotebookClass import*
from Shop import*

Note1 = Notebook('HP',56000,16,500,'Windows')
Note2 = Notebook('Apple',85000,16,720,'MacOS')
Note3 = Notebook('Asus',126000,32,100,'Linux')
ListNotebook = Shop()
ListNotebook.add_notebook(Note1)
ListNotebook.add_notebook(Note2)
ListNotebook.add_notebook(Note3)
ListNotebook.print()
