import random
from typing import (List,
                    )
from strategy_interfaces import (SortStrategy,
                                 )


class BubbleSortStrategy(SortStrategy):
    def sort(self, arr: List[int]) -> None:
        arr_len = len(arr)
        for i in range(arr_len):
            for j in range(arr_len - 1 - i):
                if arr[j + 1] < arr[j]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]

class CocktailSortStrategy(SortStrategy):
    def sort(self, arr: List[int]) -> None:
        arr_len = len(arr)
        swaped = True
        while swaped:
            swaped = False
            for i in range(arr_len - 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swaped = True

            if not swaped:
                break

            swaped = False
            for i in range(arr_len - 1, 0, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    swaped = True


class HeapSortStrategy(SortStrategy):
    def _heapify(self, arr: List[int], arr_len: int, cur_el_idx: int) -> None:
        largest = cur_el_idx
        left = 2 * cur_el_idx + 1
        right = 2 * cur_el_idx + 2

        if left < arr_len and arr[left] > arr[largest]:
            largest = left
        if right < arr_len and arr[right] > arr[largest]:
            largest = right
        if largest != cur_el_idx:
            arr[largest], arr[cur_el_idx] = arr[cur_el_idx], arr[largest]
            self._heapify(arr, arr_len, largest)
    
    def sort(self, arr: List[int]) -> None:
        arr_len = len(arr)
        for i in range(arr_len // 2, -1, -1):
            self._heapify(arr, arr_len, i)
        for i in range(arr_len - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self._heapify(arr, i, 0)

class InsertionSortStrategy(SortStrategy):
    def sort(self, arr: List[int]) -> None:
        arr_len = len(arr)
        for i in range(1, arr_len):

            for j in range(0, i+1):
                
                if arr[j] >= arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]

class MergeSortStrategy(SortStrategy):
    def _merge(self, arr: List[int], left: int, mid: int, right: int) -> None:
        # Визначаємо кількість елементів у масивах L і R
        len_l_list = mid - left + 1 
        len_r_list = right - mid

        # Копіюємо елементи з масиву arr до масивів L і R
        L = [arr[left + i] for i in range(len_l_list)]
        R = [arr[mid + 1 + j] for j in range(len_r_list)]


        i = 0
        j = 0
        k = left  # індекс з якого елемента модифікуємо оригінальний масив

        # Шукаємо найбільший/найменший елементи та розставляємо їх по місцях
        # Елементи порівнюються попарно
        while (i < len_l_list) and (j < len_r_list):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Копіюємо залишкові елементи з масиву L
        while i < len_l_list:
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Копіюємо залишкові елементи з масиву R
        while j < len_r_list:
            arr[k] = R[j]
            j += 1
            k += 1

    def _merge_sort(self, arr: List[int], left: int, right: int) -> None:

        if left < right: # допоки в масиві > 1 елемента

            mid = (left + right) // 2

            self._merge_sort(arr, left, mid) # рекурсія на розділ лівого підмасива
            self._merge_sort(arr, mid + 1, right) # рекурсія на розділ правого підмасива
            self._merge(arr, left, mid, right) # функція, для злиття підмасивів

    def sort(self, arr: List[int]) -> None:
        left = 0
        right = len(arr) - 1
        self._merge_sort(arr, left, right)

class QuickSortStrategy(SortStrategy):
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        rand_idx = random.randint(low, high)
        pivot = arr[rand_idx]
        i = low - 1
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[high], arr[i+1] = arr[i+1], arr[high]
        return i + 1
    
    def _quick_sort(self, arr: List[int], low: int, high: int) -> None:
        if low < high:
            pivot = self._partition(arr, low, high)
            self._quick_sort(arr, low, pivot - 1)
            self._quick_sort(arr, pivot + 1, high)

    def sort(self, arr: List[int]) -> None:
        low = 0
        high = len(arr) - 1
        self._quick_sort(arr, low, high)


class SelectionSortStrategy(SortStrategy):
    def sort(self, arr: List[int]) -> None:
        arr_len = len(arr)
        for i in range(arr_len-1, -1, -1):
            idx_max = i

            for j in range(i, -1, -1):
                if arr[idx_max] < arr[j]:
                    idx_max = j

            arr[i], arr[idx_max] = arr[idx_max], arr[i]

class ShellSortStrategy(SortStrategy):
    def sort(self, arr: List[int]) -> None:
        arr_len = len(arr)
        gap = arr_len // 2
        
        while (gap > 0):
            i = gap

            while(i < arr_len):
                temp = arr[i]
                j = i
            
                while(j>= gap) and (arr[j - gap] > temp):
                    arr[j] = arr[j - gap]
                    j -= gap
            
                arr[j] = temp
                i+= 1
            
            gap = gap // 2