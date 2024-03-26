def min_max_sum(arr):
    arr.sort()
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    return min_sum, max_sum

arr =[1,3,5,7,9]
min_sum, max_sum = min_max_sum(arr)
print(min_sum, max_sum)