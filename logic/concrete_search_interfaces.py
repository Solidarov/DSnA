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
