def stmc():  # single credit metro card
    return "you can use single credit metro card, Have a good trip "


class Mcc:  # metro creadit card
    def __init__(self, card):
        self.card = card
        self.func = ' '  # function
        self.payment = 0

    def get_func(self):
        func = input('chose the operation:\n1)use the card\n2)increase financial credit\n')
        self.func = func
        return self.func

    def add_money(self):
        money = 1400  # financial credit
        print(f"your financial credit is: {money}")
        if self.func == '1':
            if money >= 200:
                sum = money // 200
                print(f'you can use card {sum} times,Have a good trip')
                money -= 200
                print(f'Your cash is {money}')
            else:
                print('your financial credit is not enough')
        elif self.func == '2':
            sum = money // 200
            self.payment = int(input(f'hi, you can use card {sum} times,input money (every trip=200$)= '))
            money += self.payment
            print(f'Your cash is {money}')
        else:
            print('please enter a correct number')


class Scct(Mcc):  # subway credit card time
    def __init__(self):
        super().__init__(self)
        self.date_object = 19

    def add_money(self):
        money = 1400  # financial credit
        print(f"your financial credit is: {money}")
        if self.func == '1':
            if money >= 200:
                import datetime
                today = datetime.date.today()
                if today.day <= self.date_object:
                    sum = money // 200
                    print(f'you can use card {sum} times,Have a good trip')
                    money = money - 200
                else:
                    print(f'your card expired on {self.date_object}')
            else:
                print('your financial credit is not enough')
        elif self.func == '2':
            import datetime
            today = datetime.date.today()
            if today.day <= self.date_object:
                sum = money // 200
                self.payment = int(input(f'hi, you can use card {sum} times,input money (every trip=200$)= '))
                money = money + self.payment
            else:
                sum = money // 200
                print(f'you can use card {sum} times but your card expired on {self.date_object}')
        else:
            print('please enter a correct number')


counter = 1
while True:
    chose_card = input(
        'Chose your card:\n1)single credit metro card\n2)metro creadit card\n3)subway credit card time\n')
    if chose_card == '1':
        if counter > 0:
            print(stmc())
            counter = 0
        else:
            print('You can not use this card more than once!')
    elif chose_card == '2':
        first_card = Mcc('first_card')
        first_card.get_func()
        first_card.add_money()
    elif chose_card == '3':
        second_card = Scct()
        second_card.get_func()
        second_card.add_money()
    else:
        print('please enter a correct number')
        continue
