def merge(arr, left, mid, right):
    '''
    Функція, що відповідає за злиття двох підмасивів.
    '''
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
    

def merge_sort(arr, left, right):
    '''
    Функція, що відповідає за розділення масивів на підмасиви;
    використовує рекурсію
    '''
    if left < right: # допоки в масиві > 1 елемента

        mid = (left + right) // 2

        merge_sort(arr, left, mid) # рекурсія на розділ лівого підмасива
        merge_sort(arr, mid + 1, right) # рекурсія на розділ правого підмасива
        merge(arr, left, mid, right) # функція, для злиття підмасивів
    