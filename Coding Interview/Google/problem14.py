"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
"""

# suppose the circle's radius equals to 1,
# then lengths of the square
# surround it equal to 2.
# we then have 
# pi*r^2/(2r)**2 
#     appro to 
# points_in_circle/iterations = p 
# which leads to pi appro to 4*p 

import random

def in_circle(x, y):
    return x**2 + y**2 < 1 
    
def monte_carlo_pi(iterations):
    points_in_circle = sum([1 for _ in range(iterations) if in_circle(random.random(), random.random())])
    percentage = points_in_circle / iterations
    pi = 4*percentage
    return pi
    
print(monte_carlo_pi(500000))
    
