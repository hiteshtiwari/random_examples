def longest_parildrom(strings):
    
    def palindrom(l, r):
        while (l >= 0 and r < len(strings) and strings[l] == strings[r]):
            l -= 1
            r += 1
        return strings  [l+1:r]
    
    result = ""
    for i in range(len(strings)):
        sub1 = palindrom(i, i)
        if len(sub1) > len(result):
            result = sub1
        sub2 = palindrom(i, i+1)
        if len(sub2) > len(result):
            result = sub2
        
    return result 

print(longest_parildrom('aabaa'))