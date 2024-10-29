class Property:
    def __init__(self, id, type, price, address, bedroomNum, bathroomNum, squareFeet, lotSize=0):
        if type not in ['House', 'Condo', 'Land']:
            raise Exception('Unrecognized property type.')
        if not isinstance(price, int):
            raise Exception('Price must be a whole number')
        if not isinstance(bedroomNum, int):
            raise Exception('Number of bedrooms must be a whole number')
        if not isinstance(bathroomNum, int):
            raise Exception('Number of bathrooms must be a whole number')
        if not isinstance(squareFeet, int):
            raise Exception('Property square feet must be a whole number')
        if not isinstance(lotSize, int):
            raise Exception('Lot size must be a whole number')
        self.id=id
        self.type=type
        self.price=price
        self.address=address
        self.bedroomNum=bedroomNum
        self.bathroomNum=bathroomNum
        self.squareFeet=squareFeet
        self.lotSize=lotSize
        
    def __repr__(self):
        return f'Property(Id: {self.id}, type: {self.type}, price: {self.price}, address: {self.address},\
            bedrooms: {self.bedroomNum} bathrooms: {self.bathroomNum}, square feet: {self.squareFeet}, lot size: {self.lotSize})'