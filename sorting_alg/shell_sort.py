def shell_sort(arr: list, arr_len: int) -> None:
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
