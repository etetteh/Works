""" This is an implemetation of the naive approach for sorting the elements of
    of a list. This approach is called Bubble Sort or, sometimes Sinking Sort.
    The name bubble sort comes from the fact that at each iteration the largest
    or lowest number ends up at the position it belongs.
    The time complexity or efficiency is O(n^2).
"""

def bubble_sort(list):
    n = len(list)
    for i in range(0, n - 1):
        for j in range(0, n - 1- i):
            if (list[j] > list[j+1]):
                # swap positions
                list[j], list[j+1] = list[j+1], list[j]
    return list

ages = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(bubble_sort(ages))