import numpy as np
import time

my_array = np.random.randint(0, 2000, size=1000)
my_array = np.sort(my_array)
print(my_array)
x = 512
print("Searching for:", x)

start_time = time.time()

def binary_search(sequence, item):
    initial_index = 0
    last_index = len(sequence) - 1
    while initial_index <= last_index:
        mid = initial_index + (last_index - initial_index) // 2
        mid_value = sequence[mid]
        if mid_value == item:
            return mid
        elif item < mid_value:
            last_index = mid - 1
        else:
            initial_index = mid + 1
    return None

result = binary_search(my_array, x)
print("Found at index:", result)

ending_time = time.time()
total_time = ending_time - start_time
print(f"Time used to get the answer: {total_time * 1000:.4f} ms")