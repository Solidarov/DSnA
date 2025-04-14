import os
from sorting_alg.selection_sort import selection_sort
from sorting_alg.insertion_sort import insertion_sort
from sorting_alg.bubble_sort import bubble_sort
from sorting_alg.merge_sort import merge_sort
from sorting_alg.quick_sort import quick_sort
from sorting_alg.shell_sort import shell_sort
from sorting_alg.cocktail_sort import cocktail_sort
from sorting_alg.heap_sort import heap_sort
from array_utils import generate_random_array, manually_generate_array


if __name__ == '__main__':
    try:
        os.system('clear')
        print('Array Sort'.center(100, "="))

        while True:
            try:
                choice = int(input("\nEnter array manually (0) or generate (1):\n-> "))
                if choice == 0:
                    arr = manually_generate_array()
                    break
                elif choice == 1:
                    arr = generate_random_array()
                    break
                else:
                    print('Invalid choice. Enter 0 or 1')
            except ValueError:
                print("Invalid input. Enter 0 or 1")

        os.system('clear')
        print('Array Sort'.center(100, "="))
        while True:
            try:
                msg = (f'\nSort array with:'
                       f'\n\tselection sort(0)'
                       f'\tinsertion sort(1)'
                       f'\n\tbubble sort(2)'
                       f'\t\tmerge sort(3)'
                       f'\n\tquick sort(4)'
                       f'\t\tshell sort(5)'
                       f'\n\tcocktail sort(6)'
                       f'\theap sort(7)'
                       f'\n-> ')
                choice = int(input(msg))
                if choice == 0:
                    selection_sort(arr, len(arr))
                    break
                elif choice == 1:
                    insertion_sort(arr, len(arr))
                    break
                elif choice == 2:
                    bubble_sort(arr, len(arr))
                    break
                elif choice == 3:
                    print(f"\nOriginal array: {arr}")
                    merge_sort(arr, 0, len(arr) - 1)
                    print(f"\nSorted array: {arr}")
                    break
                elif choice == 4:
                    print(f"\nOriginal array: {arr}")
                    quick_sort(arr, 0, len(arr) - 1)
                    print(f"\nSorted array: {arr}")
                    break
                elif choice == 5:
                    print(f"Original array: {arr}")
                    shell_sort(arr, len(arr))
                    print(f"Sorted array: {arr}")
                    break
                elif choice == 6:
                    print(f"Original array: {arr}")
                    cocktail_sort(arr, len(arr))
                    print(f"Sorted array: {arr}")
                    break
                elif choice == 7:
                    print(f"Original array: {arr}")
                    heap_sort(arr, len(arr))
                    print(f"Sorted array: {arr}")
                    break
                else:
                    print('Invalid choice. Enter 0/1/2/3/4/5/6/7')
            except ValueError:
                print("Invalid input. Enter 0/1/2/3/4/5/6/7")
    
    except KeyboardInterrupt:
        os.system('clear')
        print("Close program...")