from strategy_interfaces import (SortStrategy,
                                 SearchStrategy,)
from concrete_sort_interfaces import (BubbleSortStrategy,
                                      CocktailSortStrategy,
                                      HeapSortStrategy,
                                      InsertionSortStrategy,
                                      MergeSortStrategy,
                                      QuickSortStrategy,
                                      SelectionSortStrategy,
                                      ShellSortStrategy)
from concrete_search_interfaces import (LinearSearchStrategy,
                                        LinearSearchWithBarierStrategy,
                                        BinarySearchStrategy,
                                        )


class SortFactory:
    strategies = {
        "bubble": BubbleSortStrategy,
        "cocktail": CocktailSortStrategy,
        "heap": HeapSortStrategy,
        "insertion": InsertionSortStrategy,
        "merge": MergeSortStrategy,
        "quick": QuickSortStrategy,
        "selection": SelectionSortStrategy,
        "shell": ShellSortStrategy,

    }

    @staticmethod
    def get_strategy(name: str) -> SortStrategy:
        try:
            return SortFactory.strategies[name]()
        except KeyError:
            raise ValueError(f"Unknown sort strategy: {name}")


class SearchFactory:
    strategies = {
        "linear": LinearSearchStrategy,
        "linear w/ barier": LinearSearchWithBarierStrategy,
        "binary": BinarySearchStrategy,

    }
    
    @staticmethod
    def get_strategy(name: str) -> SearchStrategy:
        try:
            return SearchFactory.strategies[name]()
        except KeyError:
            raise ValueError(f"Unknown search strategy: {name}")


class AlgorithmFactoryProducer:
    factories = {
        "sort": SortFactory,
        "search": SearchFactory,
    }  

    @staticmethod
    def get_factory(category: str):
        try:
            return AlgorithmFactoryProducer.factories[category]
        except KeyError:
            raise ValueError
