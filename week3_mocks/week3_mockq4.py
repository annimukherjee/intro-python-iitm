n1 = input()
dob1 = input().split("-")
n2 = input()
dob2 = input().split("-")

for i in range(3):
    dob1[i], dob2[i] = int(dob1[i]) , int(dob2[i])


# print(n1,dob1,n2,dob2)

# [0 , 1, 2]
# [dd,mm,yy]


if dob1[2] > dob2[2]:
    print(n1)

elif dob1[2] < dob2[2]:
    print(n2)

else:
    if dob1[1] > dob2[1]:
        print(n1)

    elif dob1[1] < dob2[1]:
        print(n2)

    else:

        if dob1[0] > dob2[0]:
            print(n1)

        elif dob1[0] < dob2[0]:
            print(n2)

        else:

            if n1 > n2:
                print(n2)
            else:
                print(n1)
                