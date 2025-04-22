from typing import (List,
                    Optional)
from strategy_interfaces import (SearchStrategy,)


class LinearSearchStrategy(SearchStrategy):
    def search(self, data: List[int], target: int) -> Optional[int]:
        for idx, value in enumerate(data):
            if value == target:
                return idx
        return None

class BinarySearchStrategy(SearchStrategy):
    def search(self, data: List[int], target: int) -> Optional[int]:
        low, high = 0, len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] == target:
                return mid
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return None

class JumpSearchStrategy(SearchStrategy):
    def search(self, data: List[int], target: int) -> Optional[int]:
        import math
        n = len(data)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and data[min(n-1, prev + step)] < target:
            prev += step
        for idx in range(prev, min(prev+step, n)):
            if data[idx] == target:
                return idx
        return None
