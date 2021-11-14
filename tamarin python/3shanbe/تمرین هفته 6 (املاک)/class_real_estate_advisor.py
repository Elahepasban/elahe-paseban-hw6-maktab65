# کلاس مشاوره املاک

class Real_estate_advisor:
    @classmethod
    def serch_home(cls, estate_list):
        field_menu = input("Hi, choose the field:\n1)type\n2)area\n3)price\ninput:")
        for i in estate_list:
            if field_menu == '1':
                type = input('choose\n1)saleable\n2)rental')
                if type == '1':
                    if i[1] == 'saleable':
                        return cls(f'This home is proper: {i}')
                elif type == '2':
                    if i[1] == 'rental':
                        return cls(f'This home is proper: {i}')
                else:
                    print('Invalid number')
                    continue
            elif field_menu == '2':
                area = input('Enter area: ')
                if i[7] == area:
                    return cls(f'This home is proper: {i}')

            elif field_menu == '3':
                price = input('Enter price: ')
                if i[15] == price:
                    return cls(f'This home is proper: {i}')
            else:
                print('invalid number.')
