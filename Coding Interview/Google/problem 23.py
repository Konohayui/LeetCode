"""
You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

def isValid(w, h, x, y):
    return (x >= 0) and (x < w) and (y >= 0) and (y < h)
    
def maze_shortest_path(maze, start, end):
    # check whether start and end are in maze 
    if (maze[start[0]][start[1]]) or (maze[end[0]][end[1]]):
        return -1
    
    x, y = start[0], start[1]
    width, height = len(maze[0]), len(maze)
    directions = [[0, 1], [0, -1], # up, down
                  [-1, 0], [1, 0]] # left, right
    maze[x][y] = True # labeled visited cell to True
    distance = 0
    hasVisited = {(x, y): distance}
    
    while len(hasVisited) > 0:
        curr_cell, curr_dist = hasVisited.popitem()
        if (curr_cell[0] == end[0]) and (curr_cell[1] == end[1]):
            return curr_dist
        
        for direct in directions:
            next_cell_x = curr_cell[0] + direct[0]
            next_cell_y = curr_cell[1] + direct[1]
            
            if isValid(width, height, next_cell_x, next_cell_y) and \
                ((next_cell_x, next_cell_y) not in hasVisited) and not maze[next_cell_x][next_cell_y]:
                maze[next_cell_x][next_cell_y] = True
                hasVisited[(next_cell_x, next_cell_y)] = curr_dist + 1 

    return -1
    
maze1 = [[False, False, False, False],
         [True, True, False, True],
         [False, False, False, False],
         [False, False, False, False]]
        
start = (3, 0)
end = (0, 0)
assert maze_shortest_path(maze1, start, end) == 7

maze2 = [[False, False, False, False],
         [True, False, False, True],
         [False, False, False, False],
         [False, False, False, False]]
        
assert maze_shortest_path(maze2, start, end) == 5

maze3 = [[False, False, False, False],
         [True, True, True, True],
         [False, False, False, False],
         [False, False, False, False]]
        
assert maze_shortest_path(maze3, start, end) == -1


