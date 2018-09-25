for num in range(-1000, 1000):

    # try to create a new object
    num_copy = num * 1

    if num is num_copy:
        print(num, "is a singleton")
    else:
        print(num, "is not a singleton")




# big_num_1   = 1000
# big_num_2   = 1000
# small_num_1 = 1
# small_num_2 = 1

# big_num_1   is big_num_2 ?
# small_num_1 is small_num_2 ?

# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]

# list_1 == list_2? True
# list_1 is list_2? False
