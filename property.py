class Property:
    def __init__(self, id, type, price, address, bedroomNum, bathroomNum, squareFeet, lotSize=0):
        self.id=id
        self.type=type
        self.price=price
        self.address=address
        self.bedroomNum=bedroomNum
        self.bathroomNum=bathroomNum
        self.squareFeet=squareFeet
        self.lotSize=lotSize
        
    def __repr__(self):
        return f'Property(Id: {self.id}, type: {self.type}, price: {self.price}, address: {self.address}, bedrooms: {self.bedroomNum} bathrooms: {self.bathroomNum}, square feet: {self.squareFeet}, lot size: {self.lotSize})'