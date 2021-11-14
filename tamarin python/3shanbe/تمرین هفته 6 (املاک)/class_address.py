class Address:

    def __init__(self, city, street, plaque, postal_code):
        self.city = city
        self.street = street
        self.plaque = plaque
        self.postal_code = postal_code

    def edition_address(self):
        edition_menu = input("Hi, choose the one that you want change it.\n1)city\n2)street\n3)"
                             "plaque\n4)postal_code\n:")
        if edition_menu == "1":
            new_city = input("Enter city name: ")
            if new_city.isalpha:
                self.city = new_city
            else:
                new_city1 = input("city name is incorrect. enter city name again: ")
                self.city = new_city1
        elif edition_menu == '2':
            new_street = input("Enter street name: ")
            if new_street.isalnum:
                self.street = new_street
            else:
                new_street1 = input("street name is incorrect. enter street name again: ")
                self.street = new_street1
        elif edition_menu == '3':
            new_plaque = input("Enter plaque number: ")
            if new_plaque.isdigit:
                self.plaque = new_plaque
            else:
                new_plaque1 = input("plaque number is incorrect. enter plaque number again: ")
                self.plaque = new_plaque1
        elif edition_menu == '4':
            new_postal_code = input("Enter postal code: ")
            if new_postal_code.isdigit:
                self.postal_code = new_postal_code
            else:
                new_postal_code1 = input("postal code is incorrect. enter postal code again: ")
                self.postal_code = new_postal_code1
        else:
            print('The number is invalid.')
        return self.city, self.street, self.plaque, self.postal_code

    def __repr__(self):
        return f'Address: {self.city}, {self.street}, {self.plaque}, {self.postal_code} .'


def correctness_address(city, street, plaque, postal_code):
    if city.isalpha:
        pass
    else:
        new_city = input("city name is incorrect. enter city name again: ")
        city = new_city
    if street.isalnum:
        pass
    else:
        new_street = input("street name is incorrect. enter street name again: ")
        street = new_street
    if plaque.isdigit:
        pass
    else:
        new_plaque = input("plaque number is incorrect. enter plaque number again: ")
        plaque = new_plaque
    if postal_code.isdigit:
        pass
    else:
        new_postal_code = input("postal code is incorrect. enter postal code again: ")
        postal_code = new_postal_code
    return city, street, plaque, postal_code
