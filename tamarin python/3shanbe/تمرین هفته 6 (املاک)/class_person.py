class Person:

    def __init__(self, name, family, email, national_code, phone_number):
        self.name = name
        self.family = family
        self.email = email
        self.national_code = national_code
        self.phone_number = phone_number

    @classmethod
    def validation_address_email(cls, email):
        if email.count('@') == 1:
            if email.endswith(".com"):
                print('Email is correct.')
            else:
                new_email1 = input(" Your email must has '.com' at the end. enter email again: ")
                email = new_email1
        else:
            new_email2 = input("Email incorrect. enter email again: ")
            email = new_email2
        return cls(email)

    @classmethod
    def validation_national_code(cls, national_code):
        if national_code.isdigit():
            if len(national_code) == 10:
                print('national_code is correct.')
            else:
                new_national_code1 = input(" Your national_code must has 10 number. "
                                           "enter national_code again: ")
                national_code = new_national_code1
        else:
            new_national_code2 = input("National_code incorrect. enter national_code again: ")
            national_code = new_national_code2
        return cls(national_code)

    def edition_person_info(self):
        edition_menu = input("Hi, choose the one that you want change it.\n1)name\n2)family\n3)email\n"
                             "4)national_code\n5)phone_number\n:")
        if edition_menu == "1":
            new_name = input("Enter name: ")
            if new_name.isalpha:
                self.name = new_name
            else:
                new_name1 = input("Name is incorrect. enter name again: ")
                self.name = new_name1
        elif edition_menu == "2":
            new_family = input("Enter family: ")
            if new_family.isalpha:
                self.family = new_family
            else:
                new_family1 = input("Family is incorrect. enter family again: ")
                self.family = new_family1
        elif edition_menu == '3':
            new_email = input("Enter email address: ")
            e = Person.validation_address_email(new_email)
            self.email = e
        elif edition_menu == '4':
            new_national_code = input("Enter national_code: ")
            n = Person.validation_national_code(new_national_code)
            self.national_code = n
        elif edition_menu == '5':
            new_phone_number = input("Enter phone_number: ")
            if new_phone_number.isdigit:
                self.phone_number = new_phone_number
            else:
                new_phone_number1 = input("Phone_number is incorrect. enter phone_number again: ")
                self.phone_number = new_phone_number1
        else:
            print('The number is invalid.')
        return self.name, self.family, self.email, self.national_code, self.phone_number

    def __str__(self):
        return f'{self.name}, {self.family}'
