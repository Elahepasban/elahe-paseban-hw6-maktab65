# کلاس معامله

class Dealing:
    def __init__(self, buyer, landlord, date_of_contract, expiration_date):
        self.buyer = buyer
        self.landlord = landlord
        self.date_of_contract = date_of_contract
        self.expiration_date = expiration_date

    @classmethod
    def rent(cls, estate):
        if estate[1] == 'rental':
            return cls(estate)

    @classmethod
    def del_rent(cls, estate, estate_list):
        del estate_list[estate]
        return cls(estate_list)

    @classmethod
    def sale(cls, estate):
        if estate[1] == 'saleable':
            return cls(estate)

    @classmethod
    def del_sale(cls, estate, estate_list):
        del estate_list[estate]
        return cls(estate_list)
