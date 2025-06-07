# Method 1: Using Sum Formula
def find_missing_number_sum(arr):
    n = len(arr) + 1  # One number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Method 2: Using XOR
def find_missing_number_xor(arr):
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0

    # XOR of all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR of all elements in the array
    for num in arr:
        xor_arr ^= num

    # Missing number is the XOR of the two results
    return xor_all ^ xor_arr

# Example usage
arr = [1, 2, 4, 5, 6]  # Missing number is 3

print("Using Sum Formula:")
print("Missing number is:", find_missing_number_sum(arr))

print("\nUsing XOR Method:")
print("Missing number is:", find_missing_number_xor(arr))
