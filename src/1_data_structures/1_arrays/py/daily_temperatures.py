import pytest

"""
Next challenge: Daily Temperatures

Given a list of daily temperatures, return a list where result[i] 
is the number of days until a strictly warmer temperature. 
If no warmer day occurs later, use 0.

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# Expected result:
[1, 1, 4, 2, 1, 1, 0, 0]

For the temperature 75 at index 2, the next warmer temperature is 76 at index 6, 
so the answer is 6 - 2 = 4.

"""

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures) - 1, -1, -1):

        # 1. Remove indices of days that are not warmer than temperatures[i].
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop(-1)

        # 2. If a warmer day remains, record how many days away it is.
        if stack:
            result[i] = stack[-1] - i

        # 3. Push the current index.
        stack.append(i)

    return result



@pytest.mark.parametrize(
    "arr, result",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([70, 70, 71], [2, 1, 0]),
        ([90, 80, 70], [0, 0, 0]),
        ([], []),
    ]
)
def test_daily_temperatures(
    arr,
    result
):
    actual = daily_temperatures(arr)
    pass_ = actual == result
    status = "PASS" if pass_ else "FAIL"
    print(f"{status}: {arr} -> {actual}, expected {result}")
    assert pass_
