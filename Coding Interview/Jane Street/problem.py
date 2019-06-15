# cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
# returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4

"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
def car(pair):
    def first_element(a, b):
        return a 
        
    return pair(first_element)
    
def cdr(pair):
    def second_element(a, b):
        return b 
        
    return pair(second_element)
    
def add(pair):
    def add_elements(a, b):
        return a + b 
        
    return pair(add_elements)
    
print(car(cons(1, 2)))
print(cdr(cons(1, 2)))
print(add(cons(1, 2)))

