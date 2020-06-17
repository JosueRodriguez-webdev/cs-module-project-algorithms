'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # if array length is less then 0 return
    print(arr)
    if len(arr) < 0:
        return

    # loop thru the array
    for idx in range(len(arr)):
        # hold the index of the values that equal 0
        if arr[idx] == 0:
            # record the index values here, if the value == 0
            arr.append(arr[idx])
            arr.pop(idx)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
