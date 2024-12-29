def insertion_sort(arr:list, arr_len:int) -> None:
    print(f"\nOriginal array: {arr}")

    for i in range(1, arr_len):

        for j in range(0, i+1):
            
            if arr[j] >= arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    
    print(f"\nSorted array: {arr}")

