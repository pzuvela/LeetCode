import pytest

"""
Next challenge: Stock Span

You’ve used a monotonic stack to look right for a greater value. 
This time, you’ll look left.

Given daily stock prices, return a list where result[i] is the number 
of consecutive days ending at day i whose prices were less than 
or equal to prices[i].

For example:

prices = [100, 80, 60, 70, 60, 75, 85]
# result = [1, 1, 1, 2, 1, 4, 6]

At price 75 (index 5), the consecutive prices 75, 60, 70, 60 
are all less than or equal to 75. The price before them is 80, so the span is 4.

Approach: Scan left to right

Keep a stack of indices. For each index i:

Pop indices while their prices are less than or equal to prices[i].

If the stack is empty, every day from index 0 through i 
belongs to the span, so result[i] = i + 1.

Otherwise, the stack’s top is the closest earlier day 
with a strictly higher price. The span is i - stack[-1].

Push i.

Your task

Complete the function without looking back at your Daily Temperatures solution:

Target: O(n) time and O(n) space.

Pay particular attention to equal prices: they count 
toward the span, so the pop condition must include equality.

"""

def stock_span(prices):
    result = [1] * len(prices)
    stack = []

    for i in range(len(prices)):

        # 1. Pop indices whose prices are <= prices[i].
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop(-1)

        # 2. Calculate the span using the remaining stack.
        if not stack:
            result[i] = i + 1
        else:
            result[i] = i - stack[-1]

        # 3. Push the current index.
        stack.append(i)

    return result


@pytest.mark.parametrize(
    "arr, result",
    [
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ([10, 20, 30], [1, 2, 3]),
        ([30, 20, 10], [1, 1, 1]),
        ([20, 20, 20], [1, 2, 3]),
        ([50], [1]),
        ([], []),
    ]
)
def test_stock_span(
    arr,
    result
):
    actual = stock_span(arr)
    pass_ = actual == result
    status = "PASS" if pass_ else "FAIL"
    print(f"{status}: {arr} -> {actual}, expected {result}")
    assert pass_
