import pytest

"""
Next Greater Element

Use  stack to solve an array problem.

Given an array of integers, return a new array where each position contains the
first greater element to its right. If there is no greater element to its right,
use -1.
"""


def next_greater(arr):
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


@pytest.mark.parametrize(
    "arr, result",
    [
        ([2, 1, 4, 3], [4, 4, -1, -1]),
        ([1, 3, 2, 4], [3, 4, 4, -1]),
        ([4, 3, 2, 1], [-1, -1, -1, -1]),
        ([2, 2, 3], [3, 3, -1]),
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
