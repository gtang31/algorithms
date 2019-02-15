"""
Input: heights = [2,1,1,2,1,2,2], V = 4, K = 3
Output: [2,2,2,3,2,2,2]
Explanation:
#       #
#       #
##  # ###
#########
 0123456    <- index

The first drop of water lands at index K = 3:

#       #
#   w   #
##  # ###
#########
 0123456    

When moving left or right, the water can only move to the same level or a lower level.
(By level, we mean the total height of the terrain plus any water in that column.)
Since moving left will eventually make it fall, it moves left.
(A droplet "made to fall" means go to a lower height than it was at previously.)

#       #
#       #
## w# ###
#########
 0123456    

Since moving left will not make it fall, it stays in place.  The next droplet falls:

#       #
#   w   #
## w# ###
#########
 0123456  

Since the new droplet moving left will eventually make it fall, it moves left.
Notice that the droplet still preferred to move left,
even though it could move right (and moving right makes it fall quicker.)

#       #
#  w    #
## w# ###
#########
 0123456  

#       #
#       #
##ww# ###
#########
 0123456  

After those steps, the third droplet falls.
Since moving left would not eventually make it fall, it tries to move right.
Since moving right would eventually make it fall, it moves right.

#       #
#   w   #
##ww# ###
#########
 0123456  

#       #
#       #
##ww#w###
#########
 0123456  

Finally, the fourth droplet falls.
Since moving left would not eventually make it fall, it tries to move right.
Since moving right would not eventually make it fall, it stays in place:

#       #
#   w   #
##ww#w###
#########
 0123456  

The final answer is [2,2,2,3,2,2,2]:

    #    
 ####### 
 ####### 
 0123456

"""
import pdb


def pour_water(heights, drops, leak):

    # pad both ends
    heights = [float('inf')]+heights+[float('inf')]
    leak += 1
    left, right = leak-1, leak+1

    while drops:
        # pdb.set_trace()
        while (heights[leak] <= heights[left]) and (heights[leak] <= heights[right]) and drops:
            # the leak is shorter than either neighbors
            heights[leak] += 1
            drops -= 1

        while (heights[left] <= heights[leak]) and drops:
            # print(heights)
            # print('heights[left]: {}, left {}'.format(heights[left], left))
            # pdb.set_trace()
            if left < 1:
                # reset
                left = leak-1
            elif heights[left-1] < heights[left]:
                left -= 1
                continue
            elif (heights[left] < heights[leak]) and (heights[left] < heights[left+1]):
                heights[left] += 1
                drops -= 1
                continue
            left -= 1
        left = leak-1

        while (heights[right] <= heights[leak] and heights[left] >= heights[leak]) and drops:
            # print(heights)
            # print('heights[right]: {}, right {}'.format(heights[right], right))
            # print([i for i in filter(lambda x: x < heights[leak], heights[leak+1:-1])])
            # pdb.set_trace()
            if right > len(heights)-2:
                right = leak+1
            elif heights[right+1] < heights[right]:
                right += 1
                continue
            elif (heights[right] < heights[right-1]) and (heights[right] < heights[leak]):
                heights[right] += 1
                drops -= 1
                continue
            right += 1
        right = leak+1

    print(heights[1:-1])
    return heights[1:-1]


# test cases
assert(pour_water([2,1,1,2,1,2,2], 4, 3) == [2,2,2,3,2,2,2])
assert(pour_water([1,2,3,4], 2, 2) == [2,3,3,4])
assert(pour_water([3,1,3], 5, 1) == [4,4,4])
assert(pour_water([4,2,2,4,1,1], 3, 3) == [4,3,4,4,1,1])
assert(pour_water([6,2,2,4,1,1], 11, 3) == [6,4,4,5,4,4])
assert(pour_water([6,4,4,4,1,10], 11, 3) == [6,6,6,6,6,10])
assert(pour_water([6,0,4,4,1,10] , 11, 1) == [6, 5, 5, 5, 5, 10])
print(pour_water([10,1,4,4,0,6] , 11, 1))