# Accept four integers as input and write a program to print these integers in non-decreasing order.
#
# The input will be four integers in four lines. The output should be a single line with all the integers separated by a single space in non-decreasing order.

l=[]
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.sort(reverse=False)
print(*l)
