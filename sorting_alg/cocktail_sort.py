def cocktail_sort(arr, arr_len):
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


if __name__ == '__main__':
    arr = [5, 1, 4, 2, 8]
    print(arr)
    cocktail_sort(arr, len(arr))
    print(arr)
