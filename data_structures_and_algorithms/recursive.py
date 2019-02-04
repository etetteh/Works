"""This function implements the recursive algorithm
    for a Fibonacci Sequence. The complexity here
    is O(n)
"""

def get_fib(pos):
#     if pos == 0 or pos == 1:
    if pos <= 1:
        return pos
    return get_fib(pos - 1) + get_fib(pos - 2)
    return -1

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
