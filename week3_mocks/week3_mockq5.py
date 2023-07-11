p = input()

l =['\'' , '\"' , "/" , "=" , ' ', ]

# print(l)

ind =True
for i in p:
    if i in l:
        ind = False
print((l[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))

if (8 <= len(p) <= 32) and (l[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') and (ind):
    print("True")
else:
    print("False")
    


