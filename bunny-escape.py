from collections import deque
import copy

def solution(map):
    num_row = len(map) - 1
    num_col = len(map[0]) - 1
    #Get shortest distance in orginal map BFS will set to infinite if there is not way through
    shortest_path =  breadth_first_search(map, num_row, num_col)
    #Loop over the map looking for 1s to flip
    for i in range(num_row + 1):
        for j in range(num_col + 1):
            if map[i][j] == 1:
                #When a 1 is found make a copy of the map so we don't flip more than one 1 at a time
                map_copy = copy.deepcopy(map)
                map_copy[i][j] = 0
                #Set shortest path equal to the min of the original map or the new map copy with one 1 flipped
                shortest_path = min(shortest_path, breadth_first_search(map_copy, num_row, num_col))
    return shortest_path


#Checks to see if the new row index or col index is out of range
def is_valid_point(row, col, num_row, num_col):
    if row < 0 or col < 0 or row > num_row or col > num_col:
        return False
    return True


def breadth_first_search(grid, num_row, num_col):
    #Lists containing the directions we can move at any given point
    row_directions = [-1, 0, 0, 1]
    col_directions = [0, -1, 1, 0]
    #Making a another grid to keep track of what points have been visited
    visited = [[False for i in range(num_col + 1)] for j in range(num_row + 1)]
    #Marking source point as visited
    visited[0][0] = True
    #Initializing queue and enqueing tuple representing source point. 
    #First number in tuple stands for row, second the column and third the distance
    queue = deque()
    queue.append((0, 0, 1))
    while queue:
        curr = queue.popleft()
        #Checking if we've made it to the end
        if curr[0] == num_row and curr[1] == num_col:
            return curr[2]
        #Creating the next layer of points to append by iterating over the directions list and adding value to the current point
        for i in range(4):
            row = curr[0] + row_directions[i]
            col = curr[1] + col_directions[i]
            #Check if new point is in range, not a 1, and has not been visited yet
            if is_valid_point(row, col, num_row, num_col) and grid[row][col] == 0 and not visited[row][col]:
                #Update visited grid so we don't visit twice
                visited[row][col] = True
                #Create the new tuple. Remember curr[2] == distance so far
                new_point_tuple = (row, col, curr[2] + 1)
                queue.append(new_point_tuple)
    #Return infinite if we can't make it through 
    return float("inf")



#should return 10
# print(solution([
#    [0, 1, 0, 1, 0, 0, 0], 
#    [0, 0, 0, 1, 0, 1, 0]
# ]))
