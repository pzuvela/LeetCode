"""

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

"""

class Solution():

    def mergeAlternately(self, word1: str, word2: str) -> str:

        _word1_n_chars: int = len(word1)
        _word2_n_chars: int = len(word2)

        _min_n_chars = min(_word1_n_chars, _word2_n_chars)
    
        _merged_word: str = ""

        for _char1, _char2 in zip(word1[:_min_n_chars + 1], word2[:_min_n_chars + 1]):
            _merged_word += f"{_char1}{_char2}"

        _merged_word += word2[_word1_n_chars:] if _word2_n_chars > _word1_n_chars else word1[_word2_n_chars:]

        return _merged_word


if __name__ == "__main__":
    assert Solution().mergeAlternately(word1="abc", word2="pqr") == "apbqcr"
    assert Solution().mergeAlternately(word1="ab", word2="pqrs") == "apbqrs"
