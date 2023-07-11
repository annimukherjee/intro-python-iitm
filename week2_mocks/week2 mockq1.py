n = int(input())
l=[]
l.append(int(input()))

l.append(int(input()))
l.append(int(input()))
# print(l)
a,b,c = False,False,False

if l[0]==0 or l[1]==0 or l[2]==0:
    a=True
if l[0]==l[1] or l[0]==l[2] or l[1]==l[2]:
    b= True
if (l[0] + l[1] + l[2] != n):
    c=True
# print("a (0 condn) - ", a , "\nb (equality condn) - ",b,"\nc (has to equal n condn) - " , c)
# print(b)
gamma = a==True or b == True or c == True

# print("\ngamma (T if UNFAIR and F is FAIR) ",gamma)
if (gamma):
    print("UNFAIR")
else:
    print("FAIR")
