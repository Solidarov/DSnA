def heapify(arr: list, arr_len: int, cur_el_idx: int) -> None:
    '''
        Функція, що перетворює масив чисел в купу (heap)
    '''
    largest = cur_el_idx
    left = 2 * cur_el_idx + 1
    right = 2 * cur_el_idx + 2

    if left < arr_len and arr[left] > arr[largest]:
        largest = left
    if right < arr_len and arr[right] > arr[largest]:
        largest = right
    if largest != cur_el_idx:
        arr[largest], arr[cur_el_idx] = arr[cur_el_idx], arr[largest]
        heapify(arr, arr_len, largest)

def heap_sort(arr: list, arr_len: int) -> None:
    '''
        Функція, що сортує масив
        методом пірамідального сортування (heap sort)
    '''
    for i in range(arr_len // 2, -1, -1):
        heapify(arr, arr_len, i)
    for i in range(arr_len - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)