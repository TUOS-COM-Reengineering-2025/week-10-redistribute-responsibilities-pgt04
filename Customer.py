class Customer:
    def __init__(self, name: str,address:str = "NO ADDRESS", phone_number:str = "NO PHONE NUMBER"):
        self._name = name
        self.address = address
        self.phone_number = phone_number

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def set_address(self, address: str):
        self.address = address
    def get_address(self):
        return self.address

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number
    def get_phone_number(self):
        return self.phone_number
