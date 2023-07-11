s=input()
v=[]
vov = ["a","e", "i", "o" ,"u", "A","E","I","O","U"]
for i in s:
    # print(i + " ", end="")
    if i in vov:
        v.append(i)
# print(v)
s_v = list(set(v))
s_v.sort()
for i in s_v:
    print(i.lower(), end ="")
    