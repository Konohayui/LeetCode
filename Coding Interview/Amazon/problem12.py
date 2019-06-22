"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, 
write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1: 1, 1, 1, 1
2: 2, 1, 1
3: 1, 2, 1
4: 1, 1, 2
5: 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

steps = {1, 3, 5}
stairs = 4

def ways(stairs, steps):
    if len(steps) == 0 or stairs == 0:
        print("Invalid steps or stairs!")
        return 0
    res = [0]*(stairs+1) 
    res[0] = 1 
    
    for i in range(stairs+1):
        res[i] += sum([res[i-s] for s in steps if i-s > 0])
        res[i] += 1 if i in steps else 0
    return res[-1]
    
print(ways(stairs, steps))
