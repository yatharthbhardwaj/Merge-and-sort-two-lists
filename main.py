list_one = [1,3,7,9,8,5]
list_two = [2,4,0,6,10]

#concatenating lists
merged_list = list_one + list_two

i = 0
def sort_lists():
    n = len(merged_list)
    #outer loop to run this for the entire length of the list.
    for each in range(0, n):
        #inner loop to compare adjacent elements and swap them
        for i in range(0, n - 1 - each):
            if merged_list[i] > merged_list[i+1]:
                place_holder = merged_list[i]
                merged_list[i] = merged_list[i+1]
                merged_list[i+1] = place_holder

    return merged_list


print(sort_lists())

#OUTPUT - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
