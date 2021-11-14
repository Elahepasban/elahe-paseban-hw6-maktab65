sentence = input(" pleas inter statement: ")
sentence_split = sentence.split()
b=set(sentence_split)
d={}
for j in b:
    y=sentence_split.count(j)
    d[j]=y
s=sorted(d.items(), key=lambda x:x[1], reverse=True)

t=3
if len(b) < 3:
    t=len(b)
for k in range(t):
    print(s[k][0],s[k][1])















