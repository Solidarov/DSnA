import random

def partition(arr, low, high):
    """
    Функція, що переносить всі елементи менші за опорний елемент
    на його ліву сторону, а всі більші - на праву сторону.
    """
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

def quick_sort(arr, low, high):
    """
    Функція, що відповідає за рекурсивне сортування масиву.
    """
    
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
