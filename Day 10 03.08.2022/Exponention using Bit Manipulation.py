
def powerOptimised(number, power):
    
    ans = 1
    
    while (power > 0):
        last_bit = (power & 1) 

        if (last_bit):
            ans = ans * number
        number = number * number
        
        power = power >> 1
        
    return ans
    
number = int(input("Enter Number : "))
power = int(input("Enter Power : "))

print(powerOptimised(number,power))