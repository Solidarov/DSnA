import os
from sorting_alg.selection_sort import selection_sort
from sorting_alg.insertion_sort import insertion_sort
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
                choice = int(input("\nSort array with selection sort (0) or insertion sort (1):\n-> "))
                if choice == 0:
                    selection_sort(arr, len(arr))
                    break
                elif choice == 1:
                    insertion_sort(arr, len(arr))
                    break
                else:
                    print('Invalid choice. Enter 0 or 1')
            except ValueError:
                print("Invalid input. Enter 0 or 1")
    
    except KeyboardInterrupt:
        os.system('clear')
        print("Close program...")