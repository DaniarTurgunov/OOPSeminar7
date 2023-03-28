class NotebookClass:
    def __init__(self, brand, price, ram , ssd, os ) -> list:
        self._brand = brand
        self._price = price
        self._ram = ram
        self._ssd = ssd
        self._os = os

    @property
    def brand(self):
        return self._brand
    
    @property
    def price(self):
        return self._price
    
    @property
    def ram(self):
        return self._ram
    
    @property
    def ssd(self):
        return self._ssd
    @property
    def os(self):
        return self._os
    
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @price.setter
    def price(self, new_price):
        self._price = new_price
    
    @ram.setter
    def ram(self, new_ram):
        self._ram = new_ram
    
    @ssd.setter
    def ssd(self, new_ssd):
        self._ssd = new_ssd

    @os.setter
    def os(self, new_os):
        self._os = new_os
