import csv


class Real_estate_advisor:

    def __int__(self):
        self.kind = " "
        self.estate = " "

    def search(self, kind):
        self.kind = kind
        self.estate = input("What do you want buy?\n1)Apartment\n2)Home\n3)Shop\n:")
        if self.kind == "buyer":
            if self.estate == '1':
                option = input("categories:\n1)area\n2)selling-price\n:")
                with open("buy-apartment.csv", newline='') as file:
                    reader = csv.reader(file)
                    res = list(map(tuple, reader))
                if option == '1':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res) - 1
                    for i in range(1, len(res)):
                        if int(res[i][1]) >= option_count_lower and int(res[i][1]) <= option_count_highest:
                            print(
                                f'owner:{res[i][0]}, area:{res[i][1]},phone:{res[i][2]}, active_inactive:{res[i][3]}'
                                f', selling-price:{res[i][4]}, rooms:{res[i][5]}, floor:{res[i][6]},'
                                f' floors:{res[i][7]}, parking:{res[i][8]}, address:{res[i][9]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite apartment;enter apartment owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "buy-apartment.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = '0'
                        model = "0"
                elif option == '2':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for j in range(1, len(res)):
                        if int(res[j][4]) >= option_count_lower and int(res[j][4]) <= option_count_highest:
                            print(
                                f'owner:{res[j][0]}, area:{res[j][1]},phone:{res[j][2]}, active_inactive:{res[j][3]}'
                                f', selling-price:{res[j][4]}, rooms:{res[j][5]}, floor:{res[j][6]},'
                                f' floors:{res[j][7]}, parking:{res[j][8]}, address:{res[j][9]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite apartment;enter apartment owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "buy-apartment.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = 0
                        model = "0"
                else:
                    print('input is incorrect! you should chose a number')
                    chose = '0'
                    model = "0"

            elif self.estate == '2':
                option = input("categories:\n1)area\n2)selling-price\n:")
                with open("buy-home.csv", newline='') as file:
                    reader = csv.reader(file)
                    res = list(map(tuple, reader))
                if option == '1':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for i in range(1, len(res)):
                        if int(res[i][1]) >= option_count_lower and int(res[i][1]) <= option_count_highest:
                            print(
                                f'owner:{res[i][0]}, area:{res[i][1]},phone:{res[i][2]}, active_inactive:{res[i][3]}'
                                f', selling-price:{res[i][4]}, rooms:{res[i][5]}, '
                                f' floors:{res[i][6]}, parking:{res[i][7]}, address:{res[i][8]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite home;enter home owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "buy-home.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = 0
                        model = "0"
                elif option == '2':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for j in range(1, len(res)):
                        if int(res[j][4]) >= option_count_lower and int(res[j][4]) <= option_count_highest:
                            print(
                                f'owner:{res[j][0]}, area:{res[j][1]},phone:{res[j][2]}, active_inactive:{res[j][3]}'
                                f', selling-price:{res[j][4]}, rooms:{res[j][5]}, '
                                f' floors:{res[j][6]}, parking:{res[j][7]}, address:{res[j][8]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite home;enter home owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "buy-home.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = '0'
                        model = "0"
                else:
                    print('input is incorrect! you should chose a number')
                    chose = '0'
                    model = "0"

            elif self.estate == '3':
                option = input("categories:\n1)area\n2)selling-price\n:")
                with open("buy-shop.csv", newline='') as file:
                    reader = csv.reader(file)
                    res = list(map(tuple, reader))
                if option == '1':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for i in range(1, len(res)):
                        if int(res[i][1]) >= option_count_lower and int(res[i][1]) <= option_count_highest:
                            print(
                                f'owner:{res[i][0]}, area:{res[i][1]},phone:{res[i][2]}, active_inactive:{res[i][3]}'
                                f', selling-price:{res[i][4]}, address:{res[i][5]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite shop;enter shop owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "buy-shop.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = '0'
                        model = "0"
                elif option == '2':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for j in range(1, len(res)):
                        if int(res[j][4]) >= option_count_lower and int(res[j][4]) <= option_count_highest:
                            print(
                                f'owner:{res[j][0]}, area:{res[j][1]},phone:{res[j][2]}, active_inactive:{res[j][3]}'
                                f', selling-price:{res[j][4]},address:{res[j][5]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite shop;enter shop owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "buy-shop.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = '0'
                        model = "0"
                else:
                    print('input is incorrect! you should chose a number')
                    chose = '0'
                    model = "0"
            else:
                print('input is incorrect!')
                chose = '0'
                model = '0'

        if self.kind == "rent":
            if self.estate == '1':
                option = input("categories:\n1)area\n2)selling-price\n:")
                with open("rent-apartment.csv", newline='') as file:
                    reader = csv.reader(file)
                    res = list(map(tuple, reader))
                if option == "1":
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for i in range(1, len(res)):
                        if int(res[i][1]) >= option_count_lower and int(res[i][1]) <= option_count_highest:
                            print(
                                f'owner:{res[i][0]}, family:{res[i][11]}, area:{res[i][1]}, phone:{res[i][2]}, '
                                f'active_inactive:{res[i][3]}, amount-rent:{res[i][4]}, monthly rent:{res[i][5]}, '
                                f'rooms:{res[i][6]}, floor:{res[i][7]}, floors:{res[i][8]}, parking:{res[i][9]}, '
                                f'address:{res[i][10]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite apartment;enter apartment owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "rent-apartment.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = '0'
                        model = "0"
                elif option == "2":
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for j in range(1, len(res)):
                        if int(res[j][4]) >= option_count_lower and int(res[j][4]) <= option_count_highest:
                            print(
                                f'owner:{res[j][0]}, area:{res[j][1]},phone:{res[j][2]}, active_inactive:{res[j][3]}'
                                f', amount-rent:{res[j][4]}, monthly rent:{res[j][5]}, rooms:{res[j][6]}, '
                                f'floor:{res[j][7]}, floors:{res[j][8]}, parking:{res[j][9]}, address:{res[j][10]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite apartment;enter apartment owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "rent-apartment.csv"
                    else:
                        print("your favorite apartment not find!")
                        chose = '0'
                        model = "0"
                else:
                    print('input is incorrect! you should chose a number')
                    chose = '0'
                    model = "0"

            elif self.estate == '2':
                option = input("categories:\n1)area\n2)selling-price\n:")
                with open("rent-home.csv", newline='') as file:
                    reader = csv.reader(file)
                    res = list(map(tuple, reader))
                if option == '1':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for i in range(1, len(res)):
                        if int(res[i][1]) >= option_count_lower and int(res[i][1]) <= option_count_highest:
                            print(
                                f'owner:{res[i][0]}, area:{res[i][1]},phone:{res[i][2]}, active_inactive:{res[i][3]}'
                                f', amount-rent:{res[i][4]}, monthly rent:{res[i][5]}, rooms:{res[i][6]}, '
                                f' floors:{res[i][7]}, parking:{res[i][8]}, address:{res[i][9]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite home;enter home owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "rent-home.csv"
                    else:
                        print("your favorite home not find!")
                        chose = '0'
                        model = "0"
                elif option == '2':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for j in range(1, len(res)):
                        if int(res[j][4]) >= option_count_lower and int(res[j][4]) <= option_count_highest:
                            print(
                                f'owner:{res[j][0]}, area:{res[j][1]},phone:{res[j][2]}, active_inactive:{res[j][3]}'
                                f', amount-rent:{res[j][4]}, monthly rent:{res[j][5]}, rooms:{res[j][6]}, '
                                f' floors:{res[j][7]}, parking:{res[j][8]}, address:{res[j][9]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite home;enter home owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "rent-home.csv"
                    else:
                        print("your favorite home not find!")
                        chose = '0'
                        model = "0"
                else:
                    print('input is incorrect! you should chose a number')
                    chose = '0'
                    model = "0"

            elif self.estate == '3':
                option = input("categories:\n1)area\n2)selling-price\n:")
                with open("rent-shop.csv", newline='') as file:
                    reader = csv.reader(file)
                    res = list(map(tuple, reader))
                if option == '1':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for i in range(1, len(res)):
                        if int(res[i][1]) >= option_count_lower and int(res[i][1]) <= option_count_highest:
                            print(
                                f'owner:{res[i][0]}, area:{res[i][1]},phone:{res[i][2]}, active_inactive:{res[i][3]}'
                                f', amount-rent:{res[i][4]}, monthly rent:{res[i][5]}, address:{res[i][6]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite shop;enter shop owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "rent-shop.csv"
                    else:
                        print("your favorite shop not find!")
                        chose = '0'
                        model = "0"
                elif option == '2':
                    option_count_highest = int(input("Input your highest favorite number:"))
                    option_count_lower = int(input("Input your lower favorite number:"))
                    counter = len(res)-1
                    for j in range(1, len(res)):
                        if int(res[j][4]) >= option_count_lower and int(res[j][4]) <= option_count_highest:
                            print(
                                f'owner:{res[j][0]}, area:{res[j][1]},phone:{res[j][2]}, active_inactive:{res[j][3]}'
                                f', amount-rent:{res[j][4]}, monthly rent:{res[j][5]}, address:{res[j][6]}')
                        else:
                            counter -= 1
                    if counter != 0:
                        chose = input("If chose your favorite shop;enter shop owner:")
                        if len(chose) == 0:
                            chose = '0'
                        model = "rent-shop.csv"
                    else:
                        print("your favorite shop not find!")
                        chose = '0'
                        model = "0"
                else:
                    print('input is incorrect! you should chose a number')
                    chose = '0'
                    model = "0"
            else:
                print('input is incorrect!')
                chose = '0'
                model = '0'

        return [chose.capitalize(), model]

    def add(self, person_state, mark):
        if mark == 'tenant_apartment':
            with open('rent-apartment.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(person_state)
                print(f)
        elif mark == 'tenant_home':
            with open('rent-home.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(person_state)
                print(f)
        elif mark == 'tenant_shop':
            with open('rent-shop.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(person_state)
                print(f)
        elif mark == 'sell_apartment':
            with open('buy-apartment.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(person_state)
                print(f)
        elif mark == 'sell_home':
            with open('buy-home.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(person_state)
                print(f)
        elif mark == 'sell_shop':
            with open('buy-shop.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(person_state)
                print(f)
        else:
            pass


# p = Real_estate_advisor()
# b = p.search("buyer")
# print(b)
# Input your highest favorite number:20
# Input your lower favorite number:30
# your favorite apartment not find!
# Traceback (most recent call last):
#   File "C:\Users\Admin\Desktop\maktab\tamarin python\3shanbe\تمرین هفته 8 (املاک با فایل)\Moshavere.py", line 223, in <module>
#     b = p.search("buyer")
#   File "C:\Users\Admin\Desktop\maktab\tamarin python\3shanbe\تمرین هفته 8 (املاک با فایل)\Moshavere.py", line 185, in search
#     return [chose, model]
# UnboundLocalError: local variable 'chose' referenced before assignment
