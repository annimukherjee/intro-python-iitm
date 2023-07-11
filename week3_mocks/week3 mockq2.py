l=[]
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))

passed=False
failed=False

for i in range (4):
    if ( ( (l[i] + l[i+1]) %2  == 0) or ( (l[i] + l[i+1]) %2  != 0) ) and ( (l[0]+l[4]) %2 ==0 or (l[0]+l[4]) % 2!=0):
        passed = True
    else:
        failed=True

if (passed and (not failed)):
    print("YES")
else:
    print("NO")
    