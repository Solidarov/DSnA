def bubble_sort(arr:list, arr_len:int) -> None:
    print(f"\nOriginal array: {arr}")

    for i in range(arr_len):
        for j in range(arr_len - 1 - i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    
    print(f"\nSorted array: {arr}")



