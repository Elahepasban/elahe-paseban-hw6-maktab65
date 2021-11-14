class Shop:

    def __init__(self, owner, area, phone, active_inactive, amount_rent, monthly_rent):
        self.owner = owner
        self.area = area
        self.phone = phone
        self.active_inactive = active_inactive
        self.amount_rent = amount_rent
        self.monthly_rent = monthly_rent

    def edition(self):
        edition_menu = input("Hi, choose the one that you want change it.*)owner *)area "
                             "*)phone *)active_inactive *)amount_rent *)monthly_rent\ninput:")
        if edition_menu.upper() == 'owner':
            new_value = input('Enter new data: ')
            self.owner = new_value
        if edition_menu.upper() == 'area':
            new_value = input('Enter new data: ')
            self.area = new_value
        if edition_menu.upper() == 'phone':
            new_value = input('Enter new data: ')
            self.phone = new_value
        if edition_menu.upper() == 'active_inactive':
            new_value = input('Enter new data: ')
            self.active_inactive = new_value
        if edition_menu.upper() == 'amount_rent':
            new_value = input('Enter new data: ')
            self.amount_rent = new_value
        if edition_menu.upper() == 'monthly_rent':
            new_value = input('Enter new data: ')
            self.monthly_rent = new_value
        # return self.landlord, self.tenant, self.area, self.address, self.active_phone, self.disable_phone, \
        #        self.price, self.type

    def __repr__(self):
        return [{self.owner}, {self.area}, {self.phone}, {self.active_inactive}, {self.amount_rent},
                {self.monthly_rent}]


class Home(Shop):
    def __init__(self, owner, area, phone, active_inactive, amount_rent, monthly_rent, rooms, floors, parking,
                 yard_area):
        super(Home, self).__init__(owner, area, phone, active_inactive, amount_rent, monthly_rent)
        self.rooms = rooms
        self.floors = floors
        self.parking = parking
        self.yard_area = yard_area

    def edition(self):
        super(Home, self).edition()
        edition_menu = input("Hi,choose the one that you want change it.*)rooms *)floors *)parking *)yard_area\ninput:")
        if edition_menu.upper() == 'rooms':
            new_value = input('Enter new data: ')
            self.rooms = new_value
        elif edition_menu.upper() == 'floors':
            new_value = input('Enter new data: ')
            self.floors = new_value
        elif edition_menu.upper() == 'parking':
            new_value = input('Enter new data: ')
            self.parking = new_value
        elif edition_menu.upper() == 'yard_area':
            new_value = input('Enter new data: ')
            self.yard_area = new_value
        else:
            print('Invalid item!')
        # return self.apartment_dict

    def __repr__(self):
        return [{self.owner}, {self.area}, {self.phone}, {self.active_inactive}, {self.amount_rent}, \
                {self.monthly_rent}, {self.rooms}, {self.floors}, {self.parking}, {self.yard_area}]


class Apartment(Home):
    def __init__(self, owner, area, phone, active_inactive, amount_rent, monthly_rent, rooms, floors, parking,
                 yard_area, floor):
        super(Home, self).__init__(owner, area, phone, active_inactive, amount_rent, monthly_rent, rooms, floors,
                                   parking, yard_area)
        self.floor = floor

    def edition(self):
        super(Apartment, self).edition()
        edition_menu = input("Hi, choose the one that you want change it.*)floor\ninput:")
        if edition_menu.upper() == 'floor':
            new_value = input('Enter new data: ')
            self.floor = new_value
        else:
            print('Invalid item!')
        # return self.house_dict

    def __repr__(self):
        return [{self.owner}, {self.area}, {self.phone}, {self.active_inactive}, {self.amount_rent}, \
                {self.monthly_rent}, {self.rooms}, {self.floor}, {self.floors}, {self.parking}, {self.yard_area}]
