def container_with_most_water(L):
    max_area = 0
    l, r = 0,len(L) -1
    
    while l < r:
        area = min(L[l], L[r]) * (r-l)
        max_area = max(max_area, area)
        if L[l] < L[r]:
            l += 1
        elif L[l] > L[r]:
            r -= 1
    
    return max_area

input = [2,6,1,5,4]
print(container_with_most_water(input))