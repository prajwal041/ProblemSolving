
a0,a1,a2 = list(map(int, input().split()))
b0,b1,b2 = list(map(int, input().split()))
A = a0,a1,a2 = [int(a0),int(a1),int(a2)]
B = b0,b1,b2 = [int(b0),int(b1),int(b2)]
alice =bob= 0
for x,y in zip(A,B):
    if x>y:alice+=1
    elif x<y:bob+=1
print(alice, bob)




# def solve(a0, a1, a2, b0, b1, b2):
#     alice = [a0, a1, a2]
#     bob = [b0, b1, b2]
#     score = [0, 0]
#     for




# #!/bin/python
#
# import sys
#
#
# a0,a1,a2 = raw_input().strip().split(' ')
# A = a0,a1,a2 = [int(a0),int(a1),int(a2)]
# b0,b1,b2 = raw_input().strip().split(' ')
# B = b0,b1,b2 = [int(b0),int(b1),int(b2)]
# alice = bob = 0
# for x,y in zip(A,B):
#     if x>y: alice += 1
#     if x<y: bob += 1
# print alice,bob
