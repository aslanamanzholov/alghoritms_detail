def max_min_from_list(l):
    minimum = float('inf')
    maximum = float('-inf')
    for item in l:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    return {"min": minimum, "max": maximum}

max_min_from_list([1,2,3,4,5,6,7,8])
