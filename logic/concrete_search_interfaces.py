from typing import (List,
                    Optional)
from strategy_interfaces import (SearchStrategy,
                                 )
from concrete_sort_interfaces import (QuickSortStrategy,
                                      )


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
        

class BinarySearchStrategy(SearchStrategy):
    def _sort_array(self, arr: List[int]) -> None:
        sorter = QuickSortStrategy()
        sorter.sort(arr)
        print(f"\nSorted array: {arr}")

    def search(self, arr: List[int], target: int) -> Optional[int]:
        self._sort_array(arr)

        arr_len = len(arr)        
        
        high = arr_len - 1
        low = 0
        while high > low:
            mid = (high + low) // 2
            if target == arr[mid]:
                return mid
            elif target > arr[mid]:
                low = mid + 1
            elif target < arr[mid]:
                high = mid - 1
            else:
                print("Something went wrong!")
