"""Binary Search: This search algorithm has an efficiency of O(log(n)).
   Typically with this algorithm, we start our search with the middle number
   of the array and compare it to our search value. in a situation, where there 
   is no exact middle number, we take the lower value of the two middle numbers.
   Now let's give it a try.
"""

def binary_search(input_array, value):
    low = 0
    high = len(input_array)-1
    while (low <= high):
        middle = (low+high)//2
        if(input_array[middle] == value):
            return middle
        elif (input_array[middle] < value):
            low = middle + 1
        else:
            high = middle - 1
    return -1

test_list = [3,5,9,22,29,32,35,54,57]
test_val1 = 60
# test_val2 = 15
print(binary_search(test_list, test_val1))
# print(binary_search(test_list, test_val2))        