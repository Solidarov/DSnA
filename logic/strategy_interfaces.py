from abc import ABC, abstractmethod
from typing import List, Optional

class SortStrategy(ABC):

    @abstractmethod
    def sort(self, arr: List[int]) -> None:
        """Sorts the list and returns a new sorted list."""
        pass

class SearchStrategy(ABC):
    
    @abstractmethod
    def search(self, arr: List[int], target: int) -> Optional[int]:
        """Searches for target in data and returns its index or None."""
        pass
