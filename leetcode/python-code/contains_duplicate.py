def find_any_duplicate(l):
    exists_val = set()
    
    for i in l:
        if i in exists_val:
            return True
        else:
            exists_val.add(i)
    return False

input_list = [3, 8,4, 6, 4,5]

print(find_any_duplicate(input_list))     