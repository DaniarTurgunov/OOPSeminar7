from NotebookClass import NotebookClass

class Notebook(NotebookClass): 
    def __init__(self, brand, price, ram, ssd, os) -> list:
        super().__init__(brand, price, ram, ssd, os)
        
    def __str__(self) :
        return f"{self.brand}, {self._price}, {self._ram}, {self._ssd}, {self._os}"   
    
    def price(self):
        return super().price
   
    def ram(self):
        return super().ram
    
    def ssd(self):
        return super().ssd
    
    def os(self):
        return super().os