# My Submission

def find_next_square(sq):
    import math
    x = math.sqrt(sq)
    if x.is_integer():
        return (x+1) ** 2
    return -1
    
- - - - - - - - - - - - - - - - - - - - 
# Description

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect

- - - - - - - - - - - - - - - - - - - - 
# Best Practice - Group Opinion

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
    
    
    
    
    #
