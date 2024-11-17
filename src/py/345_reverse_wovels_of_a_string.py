from operator import itemgetter


class Solution:

    def __init__(self):
        self.wovels = (
            "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
        )

    def reverseVowels(self, s: str) -> str:

        _indices = []
        _letters = []
        _wovels = []

        for _i, _letter in enumerate(s):
            if _letter in self.wovels:
                _indices.append(_i)
                _wovels.append(_letter)
            _letters.append(_letter)

        _wovels.reverse()

        for _idx, _wovel in zip(_indices, _wovels):
            _letters[_idx] = _wovel

        return "".join(_letters)


if __name__ == "__main__":
    assert Solution().reverseVowels(s="IceCreAm") == "AceCreIm"
