# Demonstrate a collection of list operations.

# Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    print("The original data for all functions is: ", ONE_TEN)

    # Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swap_first_last(data)
    print("After swapping first and last: ", data)

    # Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shift_right(data)
    print("After shifting right: ", data)

    # Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replace_even(data)
    print("After replacing even elements: ", data)

    # Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replace_neighbors(data)
    print("After replacing with neighbors: ", data)

    # Demonstrate removing the middle element.
    data = list(ONE_TEN)
    remove_middle(data)
    print("After removing the middle element(s): ", data)

    # Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    even_to_front(data)
    print("After moving even elements: ", data)

    # Demonstrate finding the second largest value.
    print("The second largest value is: ", second_largest(ONE_TEN))

    # Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", is_increasing(ONE_TEN))

    # Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", has_adjacent_duplicate(ONE_TEN))

    # Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", has_duplicate(ONE_TEN))

# Function swap_first_last
# Swap the first and last element in a list.
#  @param data the list of values to process
def swap_first_last(values):
    temp = values[0]
    values[0] = values[len(values) - 1]
    values[len(values) - 1] = temp

# Function shift_right
# Shift the elements to the right.
#  @param data the list of values to process
def shift_right(values):
    if len(values) > 0:
        # pop() automatically grabs the last element safely
        last_item = values.pop()  
        values.insert(0, last_item)


# Function replace_even
# Replace all even elements in the list with 0.
#  @param data the list of values to process
def replace_even(values):
    for i in range(len(values)):
        if values[i] % 2 == 0:
            values[i] = 0


# Function replace_neighbors
# Replace each value with the larger of its neighbors.
#  @param data the list of values to process
def replace_neighbors(values):
    original = values[:]
    for i in range(1, len(values) - 1):
        values[i] = max(original[i - 1], original[i + 1])



# Function  remove_middle
# Remove the middle element or elements from a list.
#  @param data the list of values to process
def remove_middle(values):
    mid = len(values) // 2  
    
    if len(values) % 2 != 0:
        values.pop(mid)
    else:
        values.pop(mid)
        values.pop(mid - 1)



# Function even_to_front
# Move even elements to the front of the list.
#  @param data the list of values to process
def even_to_front(values):
    even = []
    odd = []
    for i in range(len(values)):
        if values[i] % 2 == 0:
            even.append(values[i])
        else:
            odd.append(values[i])
    # Use [:] to overwrite the original list's contents in-place!
    values[:] = even + odd
                

# Function second_largest
# Identify the second largest value in a list.
#  @param data the list of values to process
#  @return the second largest value in the list
def second_largest(values):
    second = values[0]
    if values[1] > second:
        first = values[1]
    else:
        first = second
        second = values[1]

    for i in range(2, len(values)):
        if values[i] > first:
            second = first
            first = values[i]
        elif values[i] > second and values[i] != first:
            second = values[i]

    return second


# Function is_increasing
# Determine whether or not the list is in increasing order.
#  @param data the list of values to process
#  @return True if the list is in increasing order, False otherwise
def is_increasing(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True



# Function has_adjacent_duplicate
# Determine if the list contains adjacent duplicate elements.
#  @param data the list of values to process
#  @return True if the list contains adjacent duplicates, False otherwise
def has_adjacent_duplicate(values):
    for i in range(len(values) - 1):
        if values[i] == values[i + 1]:
            return True
    return False


# Function has_duplicate
# Determine if the lost contains duplicate elements.
#  @param data the list of values to process
#  @return True if the list contains duplicates, False otherwise
def has_duplicate(values):
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return True
    return False

main()
