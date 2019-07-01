"""
A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
return the minimum cost which achieves this goal.
"""

def min_paint_house_cost(cost_matrix):
    if not cost_matrix:
        return 0
        
    houses, colors = len(cost_matrix), len(cost_matrix[0])
    pre_house_min, pre_house_sec_min, pre_house_color = 0, 0, -1
    
    for n in range(houses):
        curr_house_min = float("inf")
        curr_sec_house_min = float("inf")
        curr_house_color = -1
                
        for c in range(colors):
            if pre_house_color == c:
                cost_matrix[n][c] += pre_house_sec_min
            else:
                cost_matrix[n][c] += pre_house_min
                
            # first optimal cost
            if cost_matrix[n][c] < curr_house_min:
                curr_sec_house_min = curr_house_min
                curr_house_min = cost_matrix[n][c]
                curr_house_color = c 
            # second optimal cost
            elif cost_matrix[n][c] < curr_sec_house_min:
                curr_sec_house_min = cost_matrix[n][c]
        
        pre_house_min = curr_house_min
        pre_house_sec_min = curr_sec_house_min
        pre_house_color = curr_house_color
        
    return min(cost_matrix[-1])
    
