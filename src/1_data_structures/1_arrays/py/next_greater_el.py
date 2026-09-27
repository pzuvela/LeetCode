import pytest

"""
Next Greater Element

Use  stack to solve an array problem.

Given an array of integers, return a new array where each position contains the
first greater element to its right. If there is no greater element to its right,
use -1.
"""


# Double loop solution
def next_greater_loop(arr):
    result = []

    # For each position i:
    #   Look at positions i + 1, i + 2, ...
    #   Find the first value greater than arr[i].
    #   If none exists, use -1.

    for i in range(len(arr)):

        for j in range(i, len(arr)):

            if arr[i] < arr[j]:
                result.append(arr[j])
                break

            else:

                if j == len(arr) - 1:
                    result.append(-1)

    return result


"""
Complexity: Your nested-loop approach takes O(n²) time in the 
worst case and O(n) space for the result.

Next step: Improve it with a stack

To reach O(n) time, scan the array from right to left. 
Keep a stack of values that might be the next greater 
element for positions farther left.

For each arr[i]:

Pop values from the stack while they are less than or equal to arr[i]. 
They cannot be the answer for this position.

If the stack is nonempty, its top is the next greater element; 
otherwise, the answer is -1.

Push arr[i] onto the stack.

"""
def next_greater(arr):

    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):

        # Remove values that are not greater than arr[i].
        # while stack and stack[-1] <= arr[i]:
        while stack and stack[-1] <= arr[i]:
            stack.pop(-1)

        # If the stack is nonempty, record its top in result[i].
        if stack:
            result[i] = stack[-1]

        # Push arr[i] onto the stack.
        stack.append(arr[i])

    return result



@pytest.mark.parametrize(
    "arr, result",
    [
        ([2, 1, 4, 3], [4, 4, -1, -1]),
        ([1, 3, 2, 4], [3, 4, 4, -1]),
        ([4, 3, 2, 1], [-1, -1, -1, -1]),
        ([2, 2, 3], [3, 3, -1]),
        ([5, 3, 4], [-1, 4, -1]),
        ([], [])
    ]
)
def test_next_greater(
    arr,
    result
):
    actual = next_greater(arr)
    pass_ = actual == result
    status = "PASS" if pass_ else "FAIL"
    print(f"{status}: {arr} -> {actual}, expected {result}")
    assert pass_
