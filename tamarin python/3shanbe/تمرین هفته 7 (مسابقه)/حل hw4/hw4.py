class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.check_answer = ''

    def validation(self, check_answer):
        self.check_answer = check_answer
        z = 0
        if self.check_answer == self.answer:
            print('Correct answer!')
            z += 1
        elif self.check_answer != self.answer:
            if self.check_answer == 0:
                print('no answer!')
                z = 0
            else:
                print('Wrong answer!')
                z -= 1
        return z

    def __dict__(self, correct, wrong, score, remaining):
        return self.question, correct, wrong, score, remaining

    def __str__(self):
        return self.question, self.answer


class TrueFalse(Quiz):
    def __str__(self):
        return self.answer


class MultipleChoice(Quiz):
    def __str__(self):
        return self.answer


class ShortAnswer(Quiz):
    def __str__(self):
        return self.answer


class Score:
    def __init__(self, score, win_status):
        self.score = score
        self.win_status = win_status

    def Total_points(self, z):
        if z == 1:
            self.score += 10
        elif z == -1:
            self.score -= 3
        else:
            self.score += 0
        print(self.score)
        return self.score

    def __str__(self):
        pass


def conter(dict_info, result, s1):
    if result == 1:
        dict_info['Q'].append(dict_info['Q'][-1] + 1)
        dict_info['correct'].append(dict_info['correct'][-1] + 1)
        dict_info['wronge'].append(dict_info['wronge'][-1] + 0)
        dict_info['score'].append(dict_info['score'][-1] + s1)
        dict_info['remaining'].append(dict_info['remaining'][-1] - 1)
    elif result == 0:
        dict_info['Q'].append(dict_info['Q'][-1] + 1)
        dict_info['correct'].append(dict_info['correct'][-1] + 0)
        dict_info['wronge'].append(dict_info['wronge'][-1] + 0)
        dict_info['score'].append(dict_info['score'][-1] + s1)
        dict_info['remaining'].append(dict_info['remaining'][-1] - 1)
    elif result == -1:
        dict_info['Q'].append(dict_info['Q'][-1] + 1)
        dict_info['correct'].append(dict_info['correct'][-1] + 0)
        dict_info['wronge'].append(dict_info['wronge'][-1] + 1)
        dict_info['score'].append(dict_info['score'][-1] + s1)
        dict_info['remaining'].append(dict_info['remaining'][-1] - 1)
    else:
        pass
    return dict_info


import csv
from pprint import pprint

dict_info = {'Q': [0], 'correct': [0], 'wronge': [0], 'score': [0], 'remaining': [5]}
with open("MultipleChoice.csv", newline='') as file:
    reader = csv.reader(file)
    res = list(map(tuple, reader))
    # pprint(res)
import random

r = random.randint(1, 5)
question1 = res[r][0]
print(f"Question No.1: {question1}\n1.{res[r][1]}\n2.{res[r][2]}\n3.{res[r][3]}\n4.{res[r][4]}")
person_answer1 = input('>>>')
correct_answer1 = res[r][5]
check_answer1 = 0
if person_answer1.isalnum():
    check_answer1 = res[r][int(person_answer1)]
else:
    check_answer1 = 0
quiz1 = Quiz(question1, correct_answer1)
result1 = quiz1.validation(check_answer1)
score1 = Score(0, 'None')
s1 = score1.Total_points(result1)
dict_info_result1 = conter(dict_info, result1, s1)
print(dict_info_result1)
while True:
    r = random.randint(1, 5)
    question2 = res[r][0]
    if question2 == question1:
        continue
    else:
        break
print(f"Question No.2: {question2}\n1.{res[r][1]}\n2.{res[r][2]}\n3.{res[r][3]}\n4.{res[r][4]}")
person_answer2 = input('>>>')
correct_answer2 = res[r][5]
check_answer2 = 0
if person_answer2.isalnum():
    check_answer2 = res[r][int(person_answer2)]
else:
    check_answer2 = 0
quiz2 = Quiz(question2, correct_answer2)
result2 = quiz2.validation(check_answer2)
score2 = Score(0, 'None')
s2 = score2.Total_points(result2)
dict_info_result2 = conter(dict_info_result1, result2, s2)
print(dict_info_result2)

with open("ShortAnswer.csv", newline='') as file:
    reader = csv.reader(file)
    res = list(map(tuple, reader))
    # pprint(res)
r = random.randint(1, 5)
question3 = res[r][0]
print(f"Question No.3: {question3}")
person_answer3 = input('>>>')
correct_answer3 = res[r][1]
check_answer3 = 0
if person_answer3.isalnum():
    check_answer3 = person_answer3
else:
    check_answer3 = 0
quiz3 = Quiz(question3, correct_answer3)
result3 = quiz3.validation(check_answer3)
score3 = Score(0, 'None')
s3 = score3.Total_points(result3)
dict_info_result3 = conter(dict_info_result2, result3, s3)
print(dict_info_result3)
while True:
    r = random.randint(1, 5)
    question4 = res[r][0]
    if question4 == question3:
        continue
    else:
        break
print(f"Question No.4: {question2}")
person_answer4 = input('>>>')
correct_answer4 = res[r][1]
check_answer4 = 0
if person_answer4.isalnum():
    check_answer4 = person_answer4
else:
    check_answer4 = 0
quiz4 = Quiz(question4, correct_answer4)
result4 = quiz4.validation(check_answer4)
score4 = Score(0, 'None')
s4 = score4.Total_points(result4)
dict_info_result4 = conter(dict_info_result3, result4, s4)
print(dict_info_result4)

with open("TrueFalse.csv", newline='') as file:
    reader = csv.reader(file)
    res = list(map(tuple, reader))
    # pprint(res)
r = random.randint(1, 5)
question5 = res[r][0]
print(f"Question No.5: {question5}\n1.True\n2.False")
person_answer5 = input('>>>')
correct_answer5 = res[r][3]
check_answer5 = 0
if person_answer5.isalnum():
    check_answer5 = res[r][int(person_answer5)]
else:
    check_answer5 = 0
quiz5 = Quiz(question5, correct_answer5)
result5 = quiz5.validation(check_answer5)
score5 = Score(0, 'None')
s5 = score5.Total_points(result5)
dict_info_result5 = conter(dict_info_result4, result5, s5)
print(dict_info_result5)
if dict_info_result5['score'][-1] > 40:
    print('You are win.')
else:
    print('You are loser.')