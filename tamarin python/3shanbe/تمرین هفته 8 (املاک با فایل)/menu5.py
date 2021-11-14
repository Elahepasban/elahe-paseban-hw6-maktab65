from Moshavere import Real_estate_advisor
from Amlak import Apartment
from Amlak import Home
from Amlak import Shop
from address import Address
from character import Person
from Dealing import Dealing

# import pandas as pd
person_list = []
# person_sell_rent = []

while True:
    try:
        menu = int(input("Who are you???\n1)I am Buyer.\n2)I want rent.\n3)I want tenant.\n4)I want sell something.\n"
                         "5)Edit informaton\n6)Exit:"))
        if menu == 1 or menu == 2 or menu == 3 or menu == 4:
            name = input("enter name:")
            family = input("enter family :")
            email = input("enter email:")
            national_code = input("enter national_code:")
            phone_number = input("enter phone_number:")
            person_account = Person(name.capitalize(), family.capitalize(), email, national_code, phone_number)
            #person_account = Person('melika', 'pas', 'ko@ut.com','0231546789', '0913475')
            person_account.validation_address_email()
            person_account.validation_national_code()
            person_list.append(person_account)
            if menu == 1:
                adam = Real_estate_advisor()
                chose_model = adam.search("buyer")
                if chose_model[0] == '0':
                    pass
                    # print(model)
                else:
                    list_del_buyer = Dealing.del_rent(chose_model[0], chose_model[1])
                    import time

                    named_tulple = time.localtime()
                    time_end = time.strftime("%m/%d/%Y+2,%H:%M:%S", named_tulple)
                    time_start = time.strftime("%m/%d/%Y,%H:%M:%S", named_tulple)
                    person_buyer = Dealing(person_account, chose_model[0], time_end, time_start)
                    # print(person_buyer)
            elif menu == 2:
                adam = Real_estate_advisor()
                chose_model = adam.search("rent")
                if chose_model[0] == '0':
                    pass
                    # print(model)
                else:
                    list_del_rent = Dealing.del_rent(chose_model[0], chose_model[1])
                    import time

                    named_tulple = time.localtime()
                    time_end = time.strftime("%m/%d/%Y+2,%H:%M:%S", named_tulple)
                    time_start = time.strftime("%m/%d/%Y,%H:%M:%S", named_tulple)
                    person_rent = Dealing(person_account, chose_model[0], time_end, time_start)
                    print(person_rent)


            elif menu == 3 or menu == 4:
                if menu == 3:
                    state = int(input("chose type of state:\n1)Apartment 2)Home 3)Shop\n:"))
                    if state == 1:
                        area = input("enter area:")
                        phone = input("enter phone:")
                        active_inactive = input("enter active or inactive:")
                        amount_rent = input("enter amount rent:")
                        monthly_rent = input("enter monthly rent:")
                        rooms = input("enter rooms:")
                        floors = input("enter floors:")
                        parking = input("enter parking:")
                        yard_area = input("enter yard area:")
                        floor = input("enter floor:")
                        person_sell_rent = Apartment(person_account, area, phone, active_inactive, amount_rent,
                                                     monthly_rent,rooms,floor,floors, parking, yard_area)
                        state_sort = 'tenant_apartment'
                    elif state == 2:
                        area = input("enter area:")
                        phone = input("enter phone:")
                        active_inactive = input("enter active or inactive:")
                        amount_rent = input("enter amount rent:")
                        monthly_rent = input("enter monthly rent:")
                        rooms = input("enter rooms:")
                        floors = input("enter floors:")
                        parking = input("enter parking:")
                        yard_area = input("enter yard area:")
                        person_sell_rent = Home(person_account, area, phone, active_inactive, amount_rent, monthly_rent,
                                                rooms,
                                                floors, parking, yard_area)
                        state_sort = 'tenant_home'
                    elif state == 3:
                        area = input("enter area:")
                        phone = input("enter phone:")
                        active_inactive = input("enter active or inactive:")
                        amount_rent = input("enter amount rent:")
                        monthly_rent = input("enter monthly rent:")
                        person_sell_rent_n = Shop(person_account, area, phone, active_inactive, amount_rent, monthly_rent)
                        person_sell_rent = person_sell_rent_n.__repr__()
                        state_sort = 'tenant_shop'
                    else:
                        print("invalid number !")

                elif menu == 4:
                    state = int(input("chose type of state:\n1)Apartment 2)Home 3)Shop\n:"))
                    if state == 1:
                        area = input("enter area:")
                        phone = input("enter phone:")
                        active_inactive = input("enter active or inactive:")
                        amount_rent = input("enter amount rent:")
                        monthly_rent = input("enter monthly rent:")
                        rooms = input("enter rooms:")
                        floors = input("enter floors:")
                        parking = input("enter parking:")
                        yard_area = input("enter yard area:")
                        floor = input("enter floor:")
                        person_sell_rent = Apartment(person_account, area, phone, active_inactive, amount_rent,
                                                     monthly_rent,
                                                     rooms, floors, parking, yard_area, floor)
                        state_sort = 'sell_apartment'
                    elif state == 2:
                        area = input("enter area:")
                        phone = input("enter phone:")
                        active_inactive = input("enter active or inactive:")
                        amount_rent = input("enter amount rent:")
                        monthly_rent = input("enter monthly rent:")
                        rooms = input("enter rooms:")
                        floors = input("enter floors:")
                        parking = input("enter parking:")
                        yard_area = input("enter yard area:")
                        person_sell_rent = Home(person_account, area, phone, active_inactive, amount_rent, monthly_rent,
                                                rooms,
                                                floors, parking, yard_area)
                        state_sort = 'sell_home'
                    elif state == 3:
                        area = input("enter area:")
                        phone = input("enter phone:")
                        active_inactive = input("enter active or inactive:")
                        amount_rent = input("enter amount rent:")
                        monthly_rent = input("enter monthly rent:")
                        person_sell_rent = Shop(person_account, area, phone, active_inactive, amount_rent, monthly_rent)
                        state_sort = 'sell_shop'
                    else:
                        print("invalid number !")

                print("enter address")
                city = input('enter city:')
                street = input('enter street:')
                plaque = input('enter plaque:')
                postal_code = input('enter postal_code:')
                person_address = Address(city, street, plaque, postal_code)
                p = person_address.__repr__()
                person_sell_rent.append(p)
                person_sell_rent_add = Real_estate_advisor()
                person_sell_rent_add.add(person_sell_rent, state_sort)

        elif menu == 5:
            pass

        elif menu == 6:
            print("finish")
            break

        else:
            print('Your chose is not defined!')
    except ValueError as m:
        print(m)
    except IndexError as m:
        print(m)
    # except TypeError:
    #     print("__str__ returned non-string (type tuple)")
