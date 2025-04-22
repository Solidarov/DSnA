from typing import (List,
                    Optional)
from strategy_interfaces import (SearchStrategy,)


class LinearSearchStrategy(SearchStrategy):
    def search(self, arr: List[int], target: int) -> Optional[int]:
        arr_len = len(arr)
        for idx in range(arr_len):
            if arr[idx] == target:
                return idx
        return None
    
class LinearSearchWithBarierStrategy(SearchStrategy):
    def search(self, arr: List[int], target:int) -> Optional[int]:
        arr_len = len(arr)
        last_value = arr[arr_len - 1]
        arr[arr_len - 1] = target

        idx = 0
        while arr[idx] != target:
            idx += 1
        arr[arr_len - 1] = last_value

        if idx < arr_len - 1 or arr[arr_len - 1] == target:
            return idx
        



