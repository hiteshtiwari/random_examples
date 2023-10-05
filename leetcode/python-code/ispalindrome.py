def ispalindrome(num):
    x = num
    if x < 0 or (x !=0 and x % 10 ==0):
        return False 
    
    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x //= 10
        
    return half == x or x == half // 10

print(ispalindrome(1221))