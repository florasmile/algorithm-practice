# Add your clarifying questions here
# an example: [1, 2, 3, 4, 5], 3
# [3, 4, 5, 1, 2]
# shift_by = 5, same list
# shift_by = 6, same as shift_by = 1, 
#########Method 2: Double reverse#########################
#TC: O(n)   SC: O(1)
def rotate_list(list, shift_by):
    shift_by = shift_by % len(list)  
    # reverse the whole list first
    reverse(list, 0, len(list) - 1)
    split_index = shift_by - 1
    # reverse each part
    reverse(list, 0, split_index)
    reverse(list, split_index + 1, len(list) - 1)
    return list

# define reverse function, revese a list from start to end index
# [1, 2, 3, 4, 5]
def reverse(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
    
    

########################Method 1##################
# TC: O(n*(k%n)), SC: O(1)
# def rotate_list(list, shift_by):
#     """
#     Shift the list by the number "shift_by"
#     Parameters: list, number (int)
#     Return: list (rotated list)
#     """
#     # assumptions: list is not empty, shift_by is a positive integer
#     # the list can contains any data types
#     # the shift_by is more than the len(list)
#     shift_by = shift_by % len(list)  
#     for i in range(shift_by):
#         rotate_list_once(list)
#     return list

# # rotate all items in a list to the right by one
# def rotate_list_once(list):
#     # [1, 2, 3, 4, 5] -> [5, 1, 2, 3, 4]
#     last_index = len(list) - 1
#     temp = list[last_index]
#     for i in range(last_index, 0, -1):
#         list[i] = list[i-1]
#     list[0] = temp
#     # print(list)

print(rotate_list([1, 2, "hello", 4, 5], 6))