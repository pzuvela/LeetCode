# Time and space complexity

**Time complexity** - how long an algorithm takes to execute.

**Space complexity** - how much memory will the algorithm require.

**What is Big O notation?**

Big O describes how an algorithm's resource usage grows as the input size increases.

For example, suppose you have an array containing one million elements.

An algorithm that checks every element may perform approximately one million operations, while an algorithm that directly accesses one element performs a constant number of operations.

| Complexity | Meaning | Example |
|---|---|---|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Traversing an array |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops over an array |

