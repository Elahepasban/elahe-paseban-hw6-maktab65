# کلاس معامله
# import pandas as pd
import csv


class Dealing:
    def __init__(self, buyer, owner, date_of_contract, expiration_date):
        self.buyer = buyer
        self.owner = owner
        self.date_of_contract = date_of_contract
        self.expiration_date = expiration_date

    @staticmethod
    def del_rent(chose, model):

        with open(model, newline='') as file:
            reader = csv.reader(file)
            res = list(map(tuple, reader))
        counter = len(res) - 1  # len(res)-1; because index[0] res is titles
        for i in range(0, len(res)):
            if res[i][0] == chose:
                a = res[i]
                del res[i]
                print(f"{a} remove from {res}")
            else:
                counter -= 1
        if counter == 0:
            print("This owner is not found!")

        return res

    def __repr__(self):
        a = f"The state of Mis/Mr {self.owner} assign to Mis/Mr {self.buyer}."
        return a

# f"The state of Mis/Mr {self.owner} assign to Mis/Mr {self.buyer}."
# a = Dealing.del_rent("zahra", 'buy-apartment.csv')
# print(a)
