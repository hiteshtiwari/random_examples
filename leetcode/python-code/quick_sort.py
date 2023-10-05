
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
    


def quick_sort(arr, l, h):
    if l < h:
        div1 = partition(arr, l, h)
        quick_sort(arr, div1 + 1, h)
        quick_sort(arr, l, div1-1)
    return arr
print(quick_sort([1,8,6,2,30,0,9,5], 0, 7))