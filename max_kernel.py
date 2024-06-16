def max_kernel(list_number,k):
    result = []
    for i in range(len(list_number)-k+1):
        result.append(max(list_number[i:i+k]))
    return result
assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]

