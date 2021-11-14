a = [{"sib": 14, "havij": 5, "moz":9},
{"sib": 3, "limu": 10},
{"havij": 6, "golabi": 8, "limu":1}]
list_tuple=[]
di=dict()
for i in a :
    for j,t in i.items():
        di[j] = di.get(j, 0) +t

print(di)