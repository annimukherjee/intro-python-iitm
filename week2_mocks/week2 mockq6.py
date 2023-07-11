s = input()
A=s.count("a")
E=s.count("e")
I=s.count("i")
O=s.count("o")
U=s.count("u")
A_i=s.find("a")
E_i=s.find("e")
I_i=s.find("i")
O_i=s.find("o")
U_i=s.find("u")

nonZero = A!=0 and E != 0 and I != 0 and O != 0 and U != 0
ind = (A_i<E_i and E_i<I_i and I_i<O_i and O_i<U_i)
count = (A>=E and E>=I and I>=O and U>=O)
if ( ind and count and nonZero):
    print("It is a perfect word")
else:
    print("It is not a perfect word")

# wrd = list(s)
# vwrd=[]
# for i in wrd:
#     if i in 'aeiou':
#         vwrd.append(i)
#
#
# print(vwrd)
