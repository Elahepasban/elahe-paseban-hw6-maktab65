n=[0, 1, 2, 3]
def dic_dic(n):
    m=n[::-1]
    first_dic={}
    for i in range(len(n)):
        first_dic={m[i]:first_dic}
    return first_dic
print(dic_dic(n))