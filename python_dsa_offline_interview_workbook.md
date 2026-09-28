# Python Data Structures & Algorithms --- Offline Interview Practice Workbook

> A self-contained practice guide for learning Python DSA with limited
> internet.
>
> **How to use this workbook:** Do not read solutions first. For each
> problem: 1. Restate the problem in your own words. 2. Write 2--4
> examples by hand. 3. Identify the likely pattern. 4. Write the
> simplest correct solution first. 5. Test edge cases. 6. Analyze time
> and space complexity. 7. Optimize only after the simple version works.

------------------------------------------------------------------------

# 0. Practice Plan

## Recommended 8-week path

### Week 1 --- Python + complexity + arrays

-   Big-O basics
-   Lists, indexing, slicing
-   Traversal
-   In-place modification
-   Prefix/suffix ideas
-   Practice Problems 1--12

### Week 2 --- Hash maps, sets, strings

-   `dict`
-   `set`
-   Counting/frequency maps
-   Membership lookup
-   Practice Problems 13--24

### Week 3 --- Two pointers + sliding window

-   Opposite-direction pointers
-   Same-direction pointers
-   Fixed windows
-   Variable windows
-   Practice Problems 25--38

### Week 4 --- Stacks, queues, monotonic stacks

-   LIFO / FIFO
-   Parentheses
-   Next greater/smaller
-   Stock span
-   Histograms
-   Practice Problems 39--52

### Week 5 --- Linked lists + binary search

-   Pointer manipulation
-   Fast/slow pointers
-   Binary search templates
-   Search on answer
-   Practice Problems 53--66

### Week 6 --- Trees, BSTs, heaps

-   DFS
-   BFS
-   Tree recursion
-   BST properties
-   Top-K
-   Practice Problems 67--82

### Week 7 --- Graphs + backtracking

-   Adjacency lists
-   DFS/BFS
-   Connected components
-   Topological sort
-   Subsets/permutations/combinations
-   Practice Problems 83--98

### Week 8 --- Dynamic programming + mixed interview sets

-   1-D DP
-   2-D DP
-   Knapsack-style thinking
-   Mixed timed practice
-   Practice Problems 99--120

## Daily routine (60--90 minutes)

-   **10 min:** review one pattern from memory.
-   **35--50 min:** solve 1--2 problems without solutions.
-   **10 min:** write complexity and mistakes.
-   **10--20 min:** redo one older problem from scratch.

If you only have 30 minutes, solve one problem and explain the algorithm
aloud.

------------------------------------------------------------------------

# 1. Python Interview Essentials

## Lists

``` python
arr = [10, 20, 30]

arr.append(40)       # add to end
arr.pop()            # remove from end
arr[-1]              # last element
len(arr)
```

Important costs:

  Operation                  Typical Complexity
  ------------------------ --------------------
  `arr[i]`                                 O(1)
  append                         amortized O(1)
  pop from end                             O(1)
  insert/delete at front                   O(n)
  `x in arr`                               O(n)
  sort                               O(n log n)

## Dictionaries

``` python
counts = {}

for value in arr:
    counts[value] = counts.get(value, 0) + 1
```

Typical lookup/insertion/deletion: **O(1) average**.

## Sets

``` python
seen = set()

if value in seen:
    ...
seen.add(value)
```

Use a set when you care about **membership** but not counts.

## Stack

Python lists work well as stacks:

``` python
stack = []
stack.append(10)
top = stack[-1]
stack.pop()
```

## Queue

Use `collections.deque`:

``` python
from collections import deque

queue = deque()
queue.append(10)
value = queue.popleft()
```

Avoid repeatedly doing `list.pop(0)` because it is O(n).

------------------------------------------------------------------------

# 2. Big-O Cheat Sheet

Common growth rates, fastest to slowest:

``` text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(2^n)
O(n!)
```

## Interview questions to ask yourself

-   How many times can each element be visited?
-   Is there a nested loop that truly performs n × n work?
-   Does a pointer only move forward?
-   Is every stack element pushed and popped at most once?
-   Am I allocating another array/map/set proportional to n?

## Important trap

A nested loop is **not automatically O(n²)**.

Example:

``` python
while stack and stack[-1] <= current:
    stack.pop()
```

If every element is pushed once and popped once over the whole
algorithm, total stack work is O(n).

------------------------------------------------------------------------

# 3. Arrays --- Foundations

## Pattern: traversal

``` python
for i in range(len(arr)):
    value = arr[i]
```

Use the index when position matters.

``` python
for value in arr:
    ...
```

Use the value directly when position does not matter.

------------------------------------------------------------------------

## Problem 1 --- Find Maximum

Return the largest number without using `max()`.

``` python
def find_max(arr):
    pass
```

Tests:

``` python
assert find_max([3, 1, 8, 2]) == 8
assert find_max([-5, -2, -10]) == -2
```

Think about what should happen for an empty list.

------------------------------------------------------------------------

## Problem 2 --- Second Largest Distinct Element

Return the second-largest **distinct** value.

``` python
def second_largest(arr):
    pass
```

Examples:

``` python
[10, 5, 8, 10] -> 8
[5, 5] -> None
```

Try: 1. sorting solution 2. O(n) one-pass solution

------------------------------------------------------------------------

## Problem 3 --- Move Zeros

Move all zeros to the end **in place**, preserving nonzero order.

``` python
def move_zeros(arr):
    pass
```

Example:

``` python
[0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
```

Target: O(n) time.

------------------------------------------------------------------------

## Problem 4 --- Remove Duplicates from Sorted Array

Modify a sorted array so each value appears once. Return the number of
unique values.

``` python
def remove_duplicates(arr):
    pass
```

Example:

``` python
[1, 1, 2, 2, 3]
# first k positions should become [1, 2, 3]
# return 3
```

Pattern: read pointer + write pointer.

------------------------------------------------------------------------

## Problem 5 --- Merge Two Sorted Arrays

``` python
def merge_sorted(a, b):
    pass
```

Example:

``` python
[1, 3, 5], [2, 4, 6] -> [1, 2, 3, 4, 5, 6]
```

Target: O(n + m).

------------------------------------------------------------------------

## Problem 6 --- Reverse Array In Place

``` python
def reverse_array(arr):
    pass
```

Do not use `arr.reverse()` or slicing.

Pattern: two pointers.

------------------------------------------------------------------------

## Problem 7 --- Rotate Array Right by k

``` python
def rotate_right(arr, k):
    pass
```

Example:

``` python
[1, 2, 3, 4, 5], k=2
-> [4, 5, 1, 2, 3]
```

Try: 1. extra array 2. reversal-based O(1) extra-space approach

------------------------------------------------------------------------

## Problem 8 --- Best Time to Buy and Sell Stock

One buy, followed later by one sell.

``` python
def max_profit(prices):
    pass
```

Example:

``` python
[7, 1, 5, 3, 6, 4] -> 5
```

Hint: remember the smallest price seen so far.

------------------------------------------------------------------------

## Problem 9 --- Product Except Self

``` python
def product_except_self(nums):
    pass
```

Example:

``` python
[1, 2, 3, 4] -> [24, 12, 8, 6]
```

Challenge: O(n), without division.

Pattern: prefix and suffix products.

------------------------------------------------------------------------

## Problem 10 --- Maximum Subarray

Find the largest sum of a contiguous subarray.

``` python
def max_subarray(nums):
    pass
```

Example:

``` python
[-2,1,-3,4,-1,2,1,-5,4] -> 6
```

The best subarray is `[4,-1,2,1]`.

Learn: Kadane's algorithm.

------------------------------------------------------------------------

## Problem 11 --- Prefix Sum Range Query

Build a structure that answers the sum from index `left` through `right`
quickly.

``` python
def build_prefix(nums):
    pass

def range_sum(prefix, left, right):
    pass
```

Goal: preprocessing O(n), each query O(1).

------------------------------------------------------------------------

## Problem 12 --- Missing Number

Array contains distinct values from `0..n`, with one missing.

``` python
def missing_number(nums):
    pass
```

Try: - set - arithmetic sum - XOR

------------------------------------------------------------------------

# 4. Hash Maps & Sets

## When to suspect hashing

Look for phrases like: - "have we seen this before?" - "frequency" -
"duplicate" - "pair that sums to..." - "group by..." - "first unique..."

------------------------------------------------------------------------

## Problem 13 --- Two Sum (Unsorted)

``` python
def two_sum(nums, target):
    pass
```

Return indices of two values adding to `target`.

Target: O(n) using a dictionary.

------------------------------------------------------------------------

## Problem 14 --- Contains Duplicate

``` python
def contains_duplicate(nums):
    pass
```

------------------------------------------------------------------------

## Problem 15 --- First Non-Repeating Character

``` python
def first_unique_char(s):
    pass
```

Return its index or `-1`.

------------------------------------------------------------------------

## Problem 16 --- Valid Anagram

``` python
def is_anagram(s, t):
    pass
```

Try: - sorting - frequency dictionary

------------------------------------------------------------------------

## Problem 17 --- Group Anagrams

``` python
def group_anagrams(words):
    pass
```

Think about a stable hashable representation of each word's letters.

------------------------------------------------------------------------

## Problem 18 --- Intersection of Arrays

Return unique values present in both arrays.

``` python
def intersection(a, b):
    pass
```

------------------------------------------------------------------------

## Problem 19 --- Majority Element

A value appears more than `n // 2` times.

``` python
def majority_element(nums):
    pass
```

First use a map. Later learn Boyer--Moore voting.

------------------------------------------------------------------------

## Problem 20 --- Longest Consecutive Sequence

``` python
def longest_consecutive(nums):
    pass
```

Example:

``` python
[100, 4, 200, 1, 3, 2] -> 4
```

Target: O(n).

Hint: only start counting at numbers that have no predecessor.

------------------------------------------------------------------------

## Problem 21 --- Isomorphic Strings

``` python
def is_isomorphic(s, t):
    pass
```

Maintain consistent mappings in both directions.

------------------------------------------------------------------------

## Problem 22 --- Word Pattern

``` python
def word_pattern(pattern, sentence):
    pass
```

Example:

``` python
"abba", "dog cat cat dog" -> True
```

------------------------------------------------------------------------

## Problem 23 --- Top K Frequent Elements

``` python
def top_k_frequent(nums, k):
    pass
```

First solve with counting + sorting. Later revisit with a heap or
buckets.

------------------------------------------------------------------------

## Problem 24 --- Subarray Sum Equals K

``` python
def subarray_sum(nums, k):
    pass
```

Count contiguous subarrays whose sum equals `k`.

Advanced hash-map pattern: prefix sum + frequency map.

------------------------------------------------------------------------

# 5. Two Pointers

## Pattern A --- opposite ends

``` python
left = 0
right = len(arr) - 1

while left < right:
    ...
```

## Pattern B --- read/write

``` python
write = 0

for read in range(len(arr)):
    ...
```

------------------------------------------------------------------------

## Problem 25 --- Two Sum in Sorted Array

``` python
def two_sum_sorted(nums, target):
    pass
```

Use `left` and `right`.

------------------------------------------------------------------------

## Problem 26 --- Valid Palindrome

Ignore punctuation and case.

``` python
def is_palindrome(s):
    pass
```

------------------------------------------------------------------------

## Problem 27 --- Squares of Sorted Array

``` python
def sorted_squares(nums):
    pass
```

Example:

``` python
[-4, -1, 0, 3, 10] -> [0, 1, 9, 16, 100]
```

------------------------------------------------------------------------

## Problem 28 --- Container With Most Water

``` python
def max_water(height):
    pass
```

Learn why moving the shorter side is correct.

------------------------------------------------------------------------

## Problem 29 --- Three Sum

Find unique triplets summing to zero.

``` python
def three_sum(nums):
    pass
```

Pattern: sort + fixed element + two pointers.

------------------------------------------------------------------------

## Problem 30 --- Remove Element

Remove a target value in place.

``` python
def remove_element(nums, target):
    pass
```

------------------------------------------------------------------------

# 6. Sliding Window

Sliding windows are useful for **contiguous** ranges.

## Fixed-size template

``` python
window_sum = sum(nums[:k])
best = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right]
    window_sum -= nums[right - k]
    best = max(best, window_sum)
```

## Variable-size template

``` python
left = 0

for right in range(len(arr)):
    # add arr[right]

    while window_is_invalid:
        # remove arr[left]
        left += 1

    # current window is valid
```

------------------------------------------------------------------------

## Problem 31 --- Maximum Sum of Size K

``` python
def max_sum_k(nums, k):
    pass
```

------------------------------------------------------------------------

## Problem 32 --- Maximum Average Subarray

``` python
def max_average(nums, k):
    pass
```

------------------------------------------------------------------------

## Problem 33 --- Longest Substring Without Repeating Characters

``` python
def longest_unique_substring(s):
    pass
```

First solve with a set.

------------------------------------------------------------------------

## Problem 34 --- Minimum Size Subarray Sum

For positive integers, find the smallest contiguous length whose sum is
at least `target`.

``` python
def min_subarray_len(target, nums):
    pass
```

------------------------------------------------------------------------

## Problem 35 --- Longest Repeating Character Replacement

``` python
def character_replacement(s, k):
    pass
```

Advanced variable-window exercise.

------------------------------------------------------------------------

## Problem 36 --- Permutation in String

``` python
def contains_permutation(s1, s2):
    pass
```

------------------------------------------------------------------------

## Problem 37 --- Find All Anagrams in a String

``` python
def find_anagrams(s, p):
    pass
```

------------------------------------------------------------------------

## Problem 38 --- Minimum Window Substring

``` python
def min_window(s, t):
    pass
```

Hard. Save this until variable windows feel comfortable.

------------------------------------------------------------------------

# 7. Stack & Queue

## Problem 39 --- Valid Parentheses

``` python
def valid_parentheses(s):
    pass
```

Examples:

``` python
"()[]{}" -> True
"([{}])" -> True
"(]" -> False
```

Use a stack of opening brackets.

------------------------------------------------------------------------

## Problem 40 --- Min Stack

Design:

``` python
class MinStack:
    def push(self, value):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def get_min(self):
        pass
```

All operations should be O(1).

------------------------------------------------------------------------

## Problem 41 --- Evaluate Reverse Polish Notation

``` python
def eval_rpn(tokens):
    pass
```

Example:

``` python
["2", "1", "+", "3", "*"] -> 9
```

------------------------------------------------------------------------

## Problem 42 --- Implement Queue Using Stacks

``` python
class MyQueue:
    pass
```

Use two stacks.

------------------------------------------------------------------------

## Problem 43 --- Implement Stack Using Queues

Use `deque`.

------------------------------------------------------------------------

# 8. Monotonic Stack

A monotonic stack maintains elements in increasing or decreasing order
so useless candidates can be discarded.

## Problem 44 --- Next Greater Element

For every value, return the first strictly greater value to its right.

``` python
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result
```

Practice tests:

``` python
assert next_greater([2, 1, 4, 3]) == [4, 4, -1, -1]
assert next_greater([5, 3, 4]) == [-1, 4, -1]
assert next_greater([2, 2, 3]) == [3, 3, -1]
```

Key lesson: the `while`, not an `if`, may need to remove multiple
useless candidates.

------------------------------------------------------------------------

## Problem 45 --- Daily Temperatures

Return the number of days until a strictly warmer day.

``` python
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures) - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1] - i

        stack.append(i)

    return result
```

Remember:

> Compare temperatures, subtract indices, push indices.

------------------------------------------------------------------------

## Problem 46 --- Stock Span

``` python
def stock_span(prices):
    result = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            result[i] = i + 1
        else:
            result[i] = i - stack[-1]

        stack.append(i)

    return result
```

------------------------------------------------------------------------

## Problem 47 --- Previous Smaller Element

For each position, find the closest smaller value to its left.

``` python
def previous_smaller(nums):
    pass
```

------------------------------------------------------------------------

## Problem 48 --- Next Smaller Element

``` python
def next_smaller(nums):
    pass
```

------------------------------------------------------------------------

## Problem 49 --- Largest Rectangle in Histogram

Start with O(n²):

``` python
def largest_rectangle(heights):
    max_area = 0

    for i in range(len(heights)):
        min_height = heights[i]

        for j in range(i, len(heights)):
            min_height = min(min_height, heights[j])
            width = j - i + 1
            area = min_height * width
            max_area = max(max_area, area)

    return max_area
```

Tests:

``` python
assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle([2, 4]) == 4
assert largest_rectangle([2, 2, 2]) == 6
assert largest_rectangle([]) == 0
```

After you can explain the brute-force version, derive the O(n)
monotonic-stack version.

------------------------------------------------------------------------

## Problem 50 --- Trapping Rain Water

``` python
def trap(height):
    pass
```

Try: 1. prefix/suffix maxima 2. two pointers 3. monotonic stack

------------------------------------------------------------------------

## Problem 51 --- Remove K Digits

Remove `k` digits to make the smallest possible number.

``` python
def remove_k_digits(num, k):
    pass
```

------------------------------------------------------------------------

## Problem 52 --- Sum of Subarray Minimums

Advanced monotonic-stack exercise.

``` python
def sum_subarray_mins(arr):
    pass
```

------------------------------------------------------------------------

# 9. Linked Lists

Use:

``` python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Essential pointer rule

Before changing a `.next`, ask:

> Will I lose access to the rest of the list?

------------------------------------------------------------------------

## Problem 53 --- Traverse Linked List

``` python
def values(head):
    pass
```

------------------------------------------------------------------------

## Problem 54 --- Reverse Linked List

``` python
def reverse_list(head):
    pass
```

Core variables:

``` python
prev = None
current = head
```

------------------------------------------------------------------------

## Problem 55 --- Find Middle Node

Use slow and fast pointers.

``` python
def middle_node(head):
    pass
```

------------------------------------------------------------------------

## Problem 56 --- Detect Cycle

Floyd's tortoise-and-hare algorithm.

``` python
def has_cycle(head):
    pass
```

------------------------------------------------------------------------

## Problem 57 --- Merge Two Sorted Linked Lists

``` python
def merge_lists(a, b):
    pass
```

------------------------------------------------------------------------

## Problem 58 --- Remove Nth Node From End

Try: 1. calculate length 2. one-pass two-pointer method

------------------------------------------------------------------------

## Problem 59 --- Palindrome Linked List

Can you do it in O(n) time and O(1) extra space?

------------------------------------------------------------------------

## Problem 60 --- Intersection of Two Linked Lists

Find the node where two lists physically join.

------------------------------------------------------------------------

# 10. Binary Search

## Standard template

``` python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Questions: - Is the search space sorted or monotonic? - What exactly
does `left` represent? - What exactly does `right` represent? - Should
the loop use `<` or `<=`?

------------------------------------------------------------------------

## Problem 61 --- Binary Search

Implement from memory.

------------------------------------------------------------------------

## Problem 62 --- First Occurrence

For duplicates, return the first index containing target.

``` python
def first_occurrence(nums, target):
    pass
```

------------------------------------------------------------------------

## Problem 63 --- Last Occurrence

------------------------------------------------------------------------

## Problem 64 --- Search Insert Position

Return where target exists or should be inserted.

------------------------------------------------------------------------

## Problem 65 --- Search Rotated Sorted Array

``` python
def search_rotated(nums, target):
    pass
```

------------------------------------------------------------------------

## Problem 66 --- Find Minimum in Rotated Sorted Array

``` python
def find_min_rotated(nums):
    pass
```

Bonus: binary search on answer problems: - integer square root - minimum
eating speed - ship packages within D days

------------------------------------------------------------------------

# 11. Trees

Use:

``` python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## DFS recursion skeleton

``` python
def dfs(node):
    if node is None:
        return

    dfs(node.left)
    dfs(node.right)
```

## BFS skeleton

``` python
from collections import deque

def bfs(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
```

------------------------------------------------------------------------

## Problem 67 --- Preorder Traversal

Order:

``` text
node -> left -> right
```

------------------------------------------------------------------------

## Problem 68 --- Inorder Traversal

``` text
left -> node -> right
```

For a BST, inorder traversal produces sorted values.

------------------------------------------------------------------------

## Problem 69 --- Postorder Traversal

``` text
left -> right -> node
```

------------------------------------------------------------------------

## Problem 70 --- Maximum Depth

``` python
def max_depth(root):
    pass
```

Solve recursively and with BFS.

------------------------------------------------------------------------

## Problem 71 --- Same Tree

``` python
def same_tree(a, b):
    pass
```

------------------------------------------------------------------------

## Problem 72 --- Invert Binary Tree

``` python
def invert_tree(root):
    pass
```

------------------------------------------------------------------------

## Problem 73 --- Level Order Traversal

Return values level by level.

``` python
def level_order(root):
    pass
```

------------------------------------------------------------------------

## Problem 74 --- Diameter of Binary Tree

Longest path between any two nodes.

------------------------------------------------------------------------

## Problem 75 --- Balanced Binary Tree

------------------------------------------------------------------------

# 12. Binary Search Trees

BST property:

``` text
left values < node < right values
```

(subject to the duplicate policy chosen by the problem).

## Problem 76 --- Search BST

## Problem 77 --- Insert Into BST

## Problem 78 --- Validate BST

Do not only compare a node to its immediate children. Track valid
bounds.

## Problem 79 --- Lowest Common Ancestor in BST

## Problem 80 --- Kth Smallest Element

Hint: inorder traversal.

------------------------------------------------------------------------

# 13. Heaps / Priority Queues

Python:

``` python
import heapq

heap = []
heapq.heappush(heap, 10)
smallest = heapq.heappop(heap)
```

`heapq` is a min-heap.

For a simple max-heap:

``` python
heapq.heappush(heap, -value)
value = -heapq.heappop(heap)
```

------------------------------------------------------------------------

## Problem 81 --- Kth Largest Element

``` python
def kth_largest(nums, k):
    pass
```

Try sorting first, then a heap.

------------------------------------------------------------------------

## Problem 82 --- Top K Frequent Elements

Revisit Problem 23 using a heap.

------------------------------------------------------------------------

## Extra heap practice

-   Merge K sorted lists
-   K closest points to origin
-   Find median from data stream
-   Task scheduler

------------------------------------------------------------------------

# 14. Graphs

Common representation:

``` python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}
```

Or for `n` numbered nodes:

``` python
graph = [[] for _ in range(n)]

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
```

## Graph DFS

``` python
def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)
```

------------------------------------------------------------------------

## Problem 83 --- DFS Traversal

## Problem 84 --- BFS Traversal

## Problem 85 --- Number of Connected Components

## Problem 86 --- Number of Islands

Grid DFS/BFS classic.

``` python
def num_islands(grid):
    pass
```

## Problem 87 --- Flood Fill

## Problem 88 --- Clone Graph

## Problem 89 --- Course Schedule

Detect whether prerequisites contain a directed cycle.

## Problem 90 --- Topological Ordering

Learn Kahn's algorithm and DFS-based ordering.

## Problem 91 --- Shortest Path in Unweighted Graph

BFS.

## Problem 92 --- Dijkstra's Algorithm

For non-negative weighted edges.

------------------------------------------------------------------------

# 15. Recursion & Backtracking

## Backtracking shape

``` python
def backtrack(path, choices):
    if solution_complete:
        result.append(path.copy())
        return

    for choice in choices:
        # choose
        path.append(choice)

        # explore
        backtrack(path, ...)

        # unchoose
        path.pop()
```

The choose → explore → unchoose structure is fundamental.

------------------------------------------------------------------------

## Problem 93 --- Factorial Recursively

## Problem 94 --- Generate Subsets

``` python
def subsets(nums):
    pass
```

## Problem 95 --- Generate Permutations

``` python
def permutations(nums):
    pass
```

## Problem 96 --- Combination Sum

## Problem 97 --- Letter Combinations of Phone Number

## Problem 98 --- N-Queens

Hard backtracking exercise.

------------------------------------------------------------------------

# 16. Dynamic Programming

DP is useful when: 1. a problem has repeated subproblems, and 2. a
larger answer can be built from smaller answers.

Ask:

> What does `dp[i]` mean?

If you cannot state that clearly, do not start coding yet.

------------------------------------------------------------------------

## Problem 99 --- Fibonacci

### Recursive

``` python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Then improve using: - memoization - bottom-up DP - O(1) space

------------------------------------------------------------------------

## Problem 100 --- Climbing Stairs

``` python
def climb_stairs(n):
    pass
```

At each step you may move 1 or 2 stairs.

------------------------------------------------------------------------

## Problem 101 --- House Robber

``` python
def rob(nums):
    pass
```

At each house: rob it and skip previous, or skip it.

------------------------------------------------------------------------

## Problem 102 --- Min Cost Climbing Stairs

## Problem 103 --- Coin Change

``` python
def coin_change(coins, amount):
    pass
```

Return minimum coins or `-1`.

## Problem 104 --- Longest Increasing Subsequence

Start with O(n²), then learn O(n log n).

## Problem 105 --- Unique Paths

Grid DP.

## Problem 106 --- Longest Common Subsequence

2-D DP.

## Problem 107 --- Edit Distance

Hard 2-D DP.

## Problem 108 --- 0/1 Knapsack

Classic DP concept.

------------------------------------------------------------------------

# 17. Sorting

Know these conceptually:

  -------------------------------------------------------------------------------
  Algorithm                 Average              Worst                Extra Space
  -------------- ------------------ ------------------ --------------------------
  Bubble sort                 O(n²)              O(n²)                       O(1)

  Insertion sort              O(n²)              O(n²)                       O(1)

  Merge sort             O(n log n)         O(n log n)                       O(n)

  Quick sort             O(n log n)              O(n²)   implementation-dependent

  Python                 O(n log n)         O(n log n)   implementation-dependent
  `sort()`               worst-case                    
  -------------------------------------------------------------------------------

You generally use Python's built-in sorting in interviews unless asked
to implement sorting.

------------------------------------------------------------------------

## Problem 109 --- Implement Merge Sort

``` python
def merge_sort(nums):
    pass
```

## Problem 110 --- Implement Quick Sort

## Problem 111 --- Sort Colors

Values are only `0`, `1`, and `2`.

Try: - counting - Dutch National Flag three-pointer solution

------------------------------------------------------------------------

# 18. Bit Manipulation

Useful operators:

``` python
a & b   # AND
a | b   # OR
a ^ b   # XOR
~a      # NOT
a << 1
a >> 1
```

Important XOR properties:

``` text
x ^ x = 0
x ^ 0 = x
```

------------------------------------------------------------------------

## Problem 112 --- Single Number

Every number appears twice except one.

``` python
def single_number(nums):
    pass
```

Target: O(n) time, O(1) extra space.

## Problem 113 --- Number of 1 Bits

## Problem 114 --- Power of Two

------------------------------------------------------------------------

# 19. Intervals

A common interview category.

Usually sort intervals by starting point first.

## Problem 115 --- Merge Intervals

``` python
def merge_intervals(intervals):
    pass
```

## Problem 116 --- Insert Interval

## Problem 117 --- Meeting Rooms

Determine whether any meetings overlap.

## Problem 118 --- Minimum Meeting Rooms

Often solved using sorting or a heap.

------------------------------------------------------------------------

# 20. Matrix / Grid Practice

## Problem 119 --- Spiral Matrix

``` python
def spiral_order(matrix):
    pass
```

## Problem 120 --- Set Matrix Zeroes

If a cell is zero, set its entire row and column to zero.

Challenge: O(1) extra space.

------------------------------------------------------------------------

# 21. Pattern Recognition Cheat Sheet

When you see...

### "pair in a sorted array"

Think:

``` text
two pointers
```

### "pair in an unsorted array"

Think:

``` text
hash map
```

### "contiguous subarray/substring"

Think:

``` text
sliding window
prefix sum
dynamic programming
```

### "next greater / previous smaller"

Think:

``` text
monotonic stack
```

### "top K / smallest K / largest K"

Think:

``` text
heap
sorting
bucket counting
```

### "sorted search"

Think:

``` text
binary search
```

### "tree level by level"

Think:

``` text
BFS + queue
```

### "tree path/depth/subtree"

Think:

``` text
DFS / recursion
```

### "shortest path in unweighted graph"

Think:

``` text
BFS
```

### "all combinations / arrangements"

Think:

``` text
backtracking
```

### "best possible result using repeated choices"

Think:

``` text
dynamic programming
greedy
```

### "frequency / duplicates / seen before"

Think:

``` text
dict / set
```

------------------------------------------------------------------------

# 22. Edge-Case Checklist

Before saying a solution is done, test:

``` text
[]
[one element]
all same values
already sorted
reverse sorted
negative values
zeros
duplicates
target absent
target at first position
target at last position
```

For strings:

``` text
""
one character
all same character
spaces/punctuation
upper/lowercase
```

For trees:

``` text
empty tree
one node
only left children
only right children
balanced tree
```

------------------------------------------------------------------------

# 23. Complexity Drill

For each snippet, state time and extra-space complexity before checking.

### A

``` python
for x in nums:
    print(x)
```

### B

``` python
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i], nums[j])
```

### C

``` python
seen = set()

for x in nums:
    if x in seen:
        return True
    seen.add(x)
```

### D

``` python
left = 0

for right in range(len(nums)):
    while left <= right and condition(nums[left], nums[right]):
        left += 1
```

### E

``` python
stack = []

for x in nums:
    while stack and stack[-1] <= x:
        stack.pop()
    stack.append(x)
```

Answers: - A: O(n) - B: O(n²) - C: O(n) average time, O(n) space - D:
usually O(n) if `left` only moves forward - E: O(n), because each
element is pushed and popped at most once

------------------------------------------------------------------------

# 24. Interview Problem-Solving Script

When given a problem, say something like this to yourself:

``` text
1. What exactly is the input and required output?
2. What edge cases matter?
3. Can I solve it by brute force?
4. What is the brute-force complexity?
5. What repeated work am I doing?
6. Is there a known pattern that removes that repeated work?
7. What invariant does my optimized solution maintain?
8. What is the final time/space complexity?
```

An optimized algorithm you cannot explain is less useful than a simple
one you understand.

------------------------------------------------------------------------

# 25. Testing Template with pytest

``` python
import pytest


def solution(arr):
    pass


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], ...),
        ([1], ...),
        ([1, 2, 3], ...),
    ]
)
def test_solution(arr, expected):
    actual = solution(arr)
    assert actual == expected
```

Run:

``` bash
pytest -q
```

For one file:

``` bash
pytest -q test_filename.py
```

------------------------------------------------------------------------

# 26. Blank Practice Templates

## Two pointers

``` python
def solve(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # inspect arr[left], arr[right]

        # move one/both pointers

        pass
```

## Sliding window

``` python
def solve(arr):
    left = 0

    for right in range(len(arr)):
        # add right

        while False:  # window invalid
            # remove left
            left += 1

        # update answer
```

## Monotonic stack

``` python
def solve(arr):
    stack = []

    for i in range(len(arr)):
        while stack and False:
            stack.pop()

        # use stack[-1] if needed

        stack.append(i)
```

## Binary search

``` python
def solve(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## Tree DFS

``` python
def dfs(node):
    if node is None:
        return

    left = dfs(node.left)
    right = dfs(node.right)

    # combine
```

## Graph BFS

``` python
from collections import deque

def bfs(start, graph):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## Backtracking

``` python
def backtrack(path):
    if False:  # complete solution
        result.append(path.copy())
        return

    for choice in []:
        path.append(choice)
        backtrack(path)
        path.pop()
```

## Memoized recursion

``` python
def solve(state, memo):
    if state in memo:
        return memo[state]

    if False:  # base case
        return ...

    answer = ...

    memo[state] = answer
    return answer
```

------------------------------------------------------------------------

# 27. Mixed Mock Interview Sets

Do these without looking at the category first.

## Set A --- Beginner

1.  Contains Duplicate
2.  Valid Palindrome
3.  Two Sum
4.  Maximum Subarray
5.  Valid Parentheses

Target: 20--25 minutes each.

## Set B --- Core

1.  Best Time to Buy/Sell Stock
2.  Longest Unique Substring
3.  Merge Intervals
4.  Binary Tree Maximum Depth
5.  Number of Islands

Target: 25--35 minutes each.

## Set C --- Stack / Pointer Focus

1.  Daily Temperatures
2.  Stock Span
3.  Three Sum
4.  Container With Most Water
5.  Largest Rectangle in Histogram

## Set D --- Intermediate

1.  Product Except Self
2.  Search Rotated Sorted Array
3.  Top K Frequent Elements
4.  Course Schedule
5.  House Robber

## Set E --- Advanced

1.  Minimum Window Substring
2.  Largest Rectangle in Histogram
3.  Coin Change
4.  Longest Common Subsequence
5.  Merge K Sorted Lists

------------------------------------------------------------------------

# 28. Redo Schedule

A problem is not mastered just because you solved it once.

After solving a problem, redo it:

``` text
Day 0  — initial solution
Day 1  — solve again without notes
Day 3  — solve again
Day 7  — solve again
Day 14 — solve again
Day 30 — final retention check
```

Mark each problem:

``` text
[ ] Never attempted
[~] Needed substantial hints
[+] Solved with a small hint
[*] Solved independently
[**] Can explain and code from memory
```

------------------------------------------------------------------------

# 29. Mistake Log

Keep a section like this while practicing:

``` text
Problem:
Date:

My mistake:
- Used value where an index was needed.

Why it happened:
- I didn't state what the stack contained.

Rule for next time:
- Before coding, write:
  "stack stores ________"
  "result[i] means ________"
```

Useful recurring mistakes to track:

-   wrong pointer movement
-   off-by-one error
-   `<` vs `<=`
-   value vs index
-   forgot empty input
-   wrong result initialization
-   modified input unexpectedly
-   returned too early
-   used `if` when repeated `while` removal was needed
-   confused substring/subarray with subsequence
-   forgot to mark graph nodes visited
-   missing recursion base case

------------------------------------------------------------------------

# 30. Core Invariants Worth Memorizing

Do not memorize whole solutions. Memorize **invariants**.

### Two pointers

``` text
Everything outside the active pointer range has already been handled.
```

### Sliding window

``` text
The current window satisfies a clearly defined condition.
```

### Monotonic stack

``` text
Every item remaining on the stack is still a possible answer for a future element.
```

### Binary search

``` text
If the target/answer exists, it remains inside the current search range.
```

### BFS

``` text
Nodes are processed in increasing distance/level from the source.
```

### DFS

``` text
Finish exploring one branch before returning to explore another.
```

### Dynamic programming

``` text
Each state has a precise meaning and is computed from already-solved smaller states.
```

------------------------------------------------------------------------

# 31. Final Offline Challenge --- 30 Problems

Try to solve these from a blank editor with no internet.

``` text
 1. Second Largest Distinct
 2. Move Zeros
 3. Two Sum
 4. Valid Anagram
 5. Best Time to Buy/Sell Stock
 6. Maximum Subarray
 7. Product Except Self
 8. Two Sum Sorted
 9. Valid Palindrome
10. Three Sum
11. Maximum Sum Window of K
12. Longest Unique Substring
13. Valid Parentheses
14. Next Greater Element
15. Daily Temperatures
16. Stock Span
17. Largest Rectangle in Histogram
18. Reverse Linked List
19. Linked List Cycle
20. Binary Search
21. Search Rotated Sorted Array
22. Maximum Depth of Binary Tree
23. Level Order Traversal
24. Validate BST
25. Kth Largest Element
26. Number of Islands
27. Course Schedule
28. Subsets
29. House Robber
30. Coin Change
```

For every problem, write these underneath your solution:

``` text
Pattern:
Time:
Space:
Key invariant:
Edge case I almost missed:
Could I explain this solution without looking at the code?
```

------------------------------------------------------------------------

# 32. What to Learn, Not Just Memorize

The goal is to reach the point where a new problem makes you think:

``` text
"This asks for a contiguous range..."
    -> sliding window / prefix sum

"I need the nearest greater value..."
    -> monotonic stack

"I repeatedly need fast membership..."
    -> set / dict

"The data is sorted..."
    -> binary search / two pointers

"I need shortest number of steps..."
    -> BFS

"I need all possible arrangements..."
    -> backtracking

"I keep recomputing the same states..."
    -> dynamic programming
```

That pattern recognition is far more valuable than memorizing 120
individual answers.

------------------------------------------------------------------------

# 33. Your Current Progress

You have already practiced these patterns/problems in our sequence:

-   Second largest distinct element
-   Move zeros
-   Remove duplicates from sorted array
-   Merge sorted arrays
-   Two Sum on a sorted array
-   Fixed sliding-window maximum sum
-   Longest substring without repeating characters
-   Valid parentheses
-   Next Greater Element --- brute force and O(n) monotonic stack
-   Daily Temperatures --- monotonic stack storing indices
-   Stock Span --- previous-greater / monotonic-stack pattern

Your next active problem is:

**Largest Rectangle in Histogram**

Start with the O(n²) version in Problem 49. Once you can implement and
explain it, derive the O(n) monotonic-stack version.

------------------------------------------------------------------------

# 34. One-Page Revision Checklist

Before an interview, make sure you can implement from memory:

``` text
[ ] dict frequency counting
[ ] set membership
[ ] two pointers
[ ] fixed sliding window
[ ] variable sliding window
[ ] stack
[ ] monotonic stack
[ ] queue / deque
[ ] linked-list reversal
[ ] fast/slow linked-list pointers
[ ] binary search
[ ] tree DFS
[ ] tree BFS
[ ] graph DFS
[ ] graph BFS
[ ] heap push/pop
[ ] backtracking
[ ] memoization
[ ] basic 1-D DP
[ ] basic 2-D DP
[ ] prefix sums
[ ] interval merging
```

And be able to explain:

``` text
[ ] O(1), O(log n), O(n), O(n log n), O(n²)
[ ] why hash lookup is O(1) average
[ ] why binary search is O(log n)
[ ] why monotonic-stack algorithms can be O(n)
[ ] recursion call-stack space
[ ] BFS vs DFS
[ ] when indices must be stored instead of values
```

------------------------------------------------------------------------

**Rule for the whole workbook:** struggle productively before checking a
solution. A 20-minute attempt followed by understanding a correction
teaches more than copying a finished answer.
