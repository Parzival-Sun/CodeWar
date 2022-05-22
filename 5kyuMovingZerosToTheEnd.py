def move_zeros(array):
    zero_count = array.count(0)
    array = [x for x in array if x != 0]
    for i in range(zero_count):
        array.append(0)
    return array


print(move_zeros([1, 1, 0, 2, 0]))
