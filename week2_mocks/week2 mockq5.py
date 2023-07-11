# Process to decide the outcome
# Team A wins if and only if the sum of its scores in both the innings is greater than sum of the scores of Team B in both the innings AND Team B lost all the ten wickets in the
# second innings. Team B wins if the sum of its scores in both the innings is greater than sum of the scores of Team A in both the innings.
# A match will end in a draw if the sum of scores in the two innings of both the teams are equal OR if Team B did not lose all the ten wickets in the second innings. If the match ends
# in a draw, then print DRAW.
# Example
# 120
# 10
# 210
# 10
# 115
# 10
# 189
# 10
# Example output
# Team A
#
# 120 + 210 > 115 + 89 and Team B lost all 10 wickets in second innings, therefore Team A is the winner of the test match.

a_s1 = int(input())
a_w1 = int(input())

a_s2 = int(input())
a_w2 = int(input())

b_s1 = int(input())
b_w1 = int(input())
b_s2 = int(input())
b_w2 = int(input())

a_total = a_s1 + a_s2
b_total = b_s1 + b_s2
b_10_wickets = b_w2==10

if (a_total>b_total and b_10_wickets):
    print("Team A")

elif (b_total>a_total):
    print("Team B")

elif (a_total==b_total or b_10_wickets==False):
    print("DRAW")