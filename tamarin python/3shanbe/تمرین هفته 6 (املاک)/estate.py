class Shop:
    def __init__(self, landlord, tenant, area, address, active_phone, disable_phone, price, type):
        self.landlord = landlord
        self.tenant = tenant
        self.area = area
        self.address = address
        self.active_phone = active_phone
        self.disable_phone = disable_phone
        self.price = price
        self.type = type

    def edition(self):
        edition_menu = input("Hi, choose the one that you want change it.*)landlord *)tenant *)area *)address "
                             "*)active_phone *)disable_phone *)price *)type\ninput:")
        if edition_menu.lower() == 'landlord':
            new_value = input('Enter new data: ')
            self.landlord = new_value
        if edition_menu.lower() == 'tenant':
            new_value = input('Enter new data: ')
            self.tenant = new_value
        if edition_menu.lower() == 'area':
            new_value = input('Enter new data: ')
            self.area = new_value
        if edition_menu.upper() == 'address':
            new_value = input('Enter new data: ')
            self.address = new_value
        if edition_menu.upper() == 'active_phone':
            new_value = input('Enter new data: ')
            self.active_phone = new_value
        if edition_menu.upper() == 'disable_phone':
            new_value = input('Enter new data: ')
            self.disable_phone = new_value
        if edition_menu.upper() == 'price':
            new_value = input('Enter new data: ')
            self.price = new_value
        if edition_menu.upper() == 'type':
            new_value = input('Enter new data: ')
            self.type = new_value
        # return self.landlord, self.tenant, self.area, self.address, self.active_phone, self.disable_phone, \
        #        self.price, self.type

    def __repr__(self):
        return 'type:', {self.type}, 'landlord:', {self.landlord}, 'tenant:', {self.tenant}, 'area:', {self.area}, \
               'address:', {self.address}, 'active_phone:', {self.active_phone}, 'disable_phone:', \
               {self.disable_phone}, 'price:', {self.price}


class House(Shop):
    def __init__(self, landlord, tenant, area, address, active_phone, disable_phone, price, type, number_of_rooms,
                 number_of_floors, parking):
        super(House, self).__init__(landlord, tenant, area, address, active_phone, disable_phone, price, type)
        self.number_of_rooms = number_of_rooms
        self.number_of_floors = number_of_floors
        self.parking = parking

    def edition(self):
        super(House, self).edition()
        edition_menu = input("Hi, choose the one that you want change it.*)landlord *)tenant "
                             "*)number of rooms *)area *)number of floors *)address "
                             "*)active_phone *)disable_phone *)price"
                             " *)type *)parking\ninput:")
        if edition_menu.upper() == 'number_of_rooms':
            new_value = input('Enter new data: ')
            self.number_of_rooms = new_value
        if edition_menu.upper() == 'number_of_floors':
            new_value = input('Enter new data: ')
            self.number_of_floors = new_value
        if edition_menu.upper() == 'parking':
            new_value = input('Enter new data: ')
            self.number_of_floors = new_value
        # else:
        #     print('Invalid item!')
        # return self.apartment_dict

    def __repr__(self):
        return 'type:', {self.type}, 'landlord:', {self.landlord}, 'tenant:', {self.tenant}, 'area:', {self.area}, \
               'address:', {self.address}, 'active_phone:', {self.active_phone}, 'disable_phone:', \
               {self.disable_phone}, 'price:', {self.price}, 'number_of_rooms:', {self.number_of_rooms}, \
               'number_of_floors:', {self.number_of_floors}, 'parking:', {self.parking}


class Apartment(House):
    def __init__(self, landlord, tenant, area, address, active_phone, disable_phone, price, type, number_of_rooms,
                 number_of_floors, parking, floor):
        super(Apartment, self).__init__(landlord, tenant, area, address, active_phone, disable_phone, price, type,
                                        number_of_rooms, number_of_floors, parking)
        self.floor = floor

    def edition(self):
        super(Apartment, self).edition()
        edition_menu = input("Hi, choose the one that you want change it.*)landlord *)tenant "
                             "*)number of rooms *)area *)number of floors *)address *)active_phone *)disable_phone "
                             "*)price *)type *)floor\ninput:")
        if edition_menu.upper() == 'floor':
            new_value = input('Enter new data: ')
            self.floor = new_value
        else:
            print('Invalid item!')
        # return self.house_dict

    def __repr__(self):
        return 'type:', {self.type}, 'landlord:', {self.landlord}, 'tenant:', {self.tenant}, 'area:', {self.area}, \
               'address:', {self.address}, 'active_phone:', {self.active_phone}, 'disable_phone:', \
               {self.disable_phone}, 'price:', {self.price}, 'number_of_rooms:', {
                   self.number_of_rooms}, 'number_of_floors:', \
               {self.number_of_floors}, 'parking:', {self.parking}, 'floor:', {self.floor}
