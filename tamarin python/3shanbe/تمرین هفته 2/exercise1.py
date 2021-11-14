def number_of_vowels(s,a):
    return s.count(a)

statement = input(" pleas inter statement: ")
statement_split = statement.split()
print(statement_split)

word = ["a","e","o","i","u"]
n_vowels = 0
for t in word:
    n_vowels += number_of_vowels(statement,t)

print("number of vowel:",n_vowels)



special = ["@","#","$","%","&"]
spt = 0
k = " "
for j in special:
    spt += number_of_vowels(statement,j)
    for i in spt:
        K += j
        print()

print("number of special carekter :",spt)


def capit(ss_plit):
    cap = " "
    for j in ss_plit:
        cap = cap +" "+ j.capitalize()
    return cap

print(capit(statement_split))














