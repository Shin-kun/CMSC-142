list_sample = [4,20,1,5,9,10]

count = 0
list_sample_length = len(list_sample)

print('unsorted list: ', list_sample)

while count < list_sample_length:
    minimum = list_sample[count]
    count_inner = count
    
    while count_inner < list_sample_length:
        if list_sample[count_inner] < minimum:
            minimum = list_sample[count_inner]
            minimum_index = count_inner
        count_inner += 1

    temp = list_sample[count]
    list_sample[count] = minimum
    list_sample[minimum_index] = temp
    count += 1

print('sorted list: ', list_sample)
