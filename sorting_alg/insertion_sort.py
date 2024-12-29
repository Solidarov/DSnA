def insertion_sort(arr:list, arr_len:int):
    for i in range(1, arr_len):
        for j in range(0, i+1):
            if arr[j] >= arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print(arr)


if __name__ == '__main__':
    arr = [5, -8, 13, 2, 44, 11, -134, 4]
    insertion_sort(arr, len(arr))
