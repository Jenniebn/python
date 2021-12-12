# Part A
def str_to_list(my_str):
    '''
    str_to_list() takes a string as an input parameter.
    - If the string has an even number of characters, return two lists,
      one containing each character of the first half of the string
      and the other containing each character of the second half of the string.
    - If the string has an odd number of characters, return two lists that
      cut the string in half as above. Odd strings will have lengths 2n+1.
      When returning, have the first list contain the first n+1 characters
      and the second list contain the last n characters.
    '''
    lst = list(my_str)
    if len(my_str) % 2 == 0:
        first = lst[:len(my_str) // 2]
        second = lst[len(my_str) // 2:]
    else:
        first = lst[:len(my_str) // 2 + 1]
        second = lst[len(my_str) // 2 + 1:]
    return first, second


def list_nester(my_lst):
    '''
    list_nester() takes a list as an input parameter.
    - Return a list that contains each element from the input list
      nested into another list.
    - If an empty list is passed into the function as the argument,
      return an empty list.
    '''
    if len(my_lst) == 0:
        return []
    else:
        newList = [list(i) for i in my_lst]
        return newList


# Part B
def perimeter_sum(my_array):
    '''
    perimeter_sum() takes an NxM nested list containing integers as input.
    - The function calculates the sum around the "perimeter" of the array
      and returns this value.
    '''
    topSum = sum(my_array[0])
    bottomSum = sum(my_array[-1])
    firstRow = True
    lastRow = True
    middleSum = 0
    for index, row in enumerate(my_array):
        if firstRow:
            firstRow = False
            continue
        if index != len(my_array) - 1:
            middleSum += my_array[index][0] + my_array[index][-1]
    total = topSum + bottomSum + middleSum
    return total
