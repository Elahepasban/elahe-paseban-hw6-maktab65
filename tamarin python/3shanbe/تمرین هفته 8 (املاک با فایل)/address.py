class Address:
    def __init__(self, city, street, plaque, postal_code):
        self.city = city
        self.street = street
        self.plaque = plaque
        self.postal_code = postal_code

    def edit_address(self):
        edit = int(input("Which part of the address do you want to edit?\n1)city 2)street 3)plaque 4)postal_code"))
        if edit == 1:
            city = input("enter your new city:")
            self.city = city
            return (self.city)
            # address.replace(self.city,edit)
        elif edit == 2:
            street = input("enter your new street:")
            self.street = street
            return (self.street)
            # address.replace(self.street,edit)
        elif edit == 3:
            plaque = input("enter your new number plaque:")
            self.plaque = plaque
            return (self.plaque)
            # address.replace(self.number_plate,edit)
        elif edit == 4:
            postal_code = input("enter your new postal_code:")
            self.postal_code = postal_code
            return (self.postal_code)
            # address.replace(self.postal_code,edit)
        else:
            print("Please select the part of the address you want to change."
                  "If you want to change the whole address Start with the name of the city and change"
                  " the information of each part")
        # return self.city, self.street, self.number_plate, self.postal_code

    def __repr__(self):
        return f'{self.city}, {self.street}, {self.plaque}, {self.postal_code}'
