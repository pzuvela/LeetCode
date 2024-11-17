class Solution:
    def reverseWords(self, s: str) -> str:
        _s = s.split(" ")
        _s.reverse()
        _reversed_string = []
        for __s in _s:
            if __s != "":
                _reversed_string.append(__s)
        return " ".join(_reversed_string)


if __name__ == "__main__":
    assert Solution().reverseWords("a good   example") == "example good a"
