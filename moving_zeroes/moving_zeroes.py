'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    if len(arr) < 0:
        return

    for idx in range(len(arr)-1, -1, -1):
        print(idx, arr)
        if arr[idx] == 0:
            arr.append(arr[idx])
            arr.pop(idx)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
