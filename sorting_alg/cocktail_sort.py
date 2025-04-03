def cocktail_sort(arr: list, arr_len: int) -> None:
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
