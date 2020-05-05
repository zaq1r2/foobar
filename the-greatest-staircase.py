def solution(n):
    #Build ways table to hold previous ways of building staircase
    ways = [[0 for i in range(n + 1)] for j in range(n + 1)]
    ways[0][0] = 1  # set base case

    #Last stands for the height of the last stair we laid down. Left stands for how many are left over after
    #So ways[last][left] would tell you have many staircases you could build if the highest stair of the staircase has height last 
    #and you have left bricks still to work with
    for last in range(1, n + 1):
        for left in range(0, n + 1):
            #Guaranteed to be able to make to make same amount of stairs as last step
            ways[last][left] = ways[last - 1][left]
            #If the bricks we have left are greater or equal to what we laid down we can build
            #The amount of extra stairs cannot be greater than last - 1. 
            #We have left - last bricks to make the new stairs and that value was already computed in the ways table so we simply look it up
            if left >= last:
                ways[last][left] += ways[last - 1][left - last]

    return ways[n][n] - 1 #subtract out invalid base case stairs must have atleast two stairs 

print(solution(5))



