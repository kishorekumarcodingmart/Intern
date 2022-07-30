def climbStairs(n):
        
    if n == 1 or n == 2:
        return n
    
    one = 1
    two = 2

    current = 0
    
    for i in range(3, n+1):
        current = one + two

        one = two
        two = current

    return current
    
print(climbStairs(5))