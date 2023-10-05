def product_array_except_self(l):
    length_array = len(l)
    product = [1] * length_array
    
    for i in range(1, length_array):
        product[i] = product[i-1] * l[i-1]
        
    print(product)
    right = l[-1]
    for j in range(length_array-2, -1, -1):
        product[j] = product[j] * right
        right = right * l[j]
        
    return product
    
print(product_array_except_self([2,3,4,5,6]))