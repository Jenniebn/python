def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        if target - num1 in seen:
            return [seen[num2], i]
        else:
            seen[num1] = i
    return []

def isAnagram(str1, str2):
    """
    :type str1: str
    :type str2: str
    :return type: bool
    """
    list1 = [items for items in str1]
    for char in str2:
        if char in list1[:]:
            list1.remove(char)
        else:
            return False
    if not list1: #if list1 is empty
        return True
    else:
        return False

def edit_dict(my_dict, my_list):
    new_dic = {}
    for key in my_dict:
        if key not in my_list:
            new_dic[key] = my_dict[key]
    return new_dic
