from typing import List
from itertools import groupby


class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        _flowerbed_length: int = len(flowerbed)

        for _i in range(_flowerbed_length):

            # Flowers can only be placed to places in flower bed with zeros
            if flowerbed[_i] == 0:
                # If first
                if (_i == 0 or flowerbed[_i - 1] == 0) and (_i == _flowerbed_length - 1 or flowerbed[_i + 1] == 0):
                    flowerbed[_i] = 1
                    n -= 1

            if n == 0:
                return True

        return False


if __name__ == "__main__":
    assert Solution().canPlaceFlowers([0,0,1,0,1], 1)
    print("\n")
    assert not Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)
    print("\n")
    assert not Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
    print("\n")
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2)
