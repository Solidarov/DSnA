import random
import os

random.seed(42)

def generate_random_list() -> list:
        max_num = input("\nEnter the max number that array can contain:\n-> ")
        max_num = int(max_num) if max_num.isdigit() else 0

        arr_len = input("\nEnter the length of the array:\n-> ")
        arr_len = int(arr_len) if arr_len.isdigit() else 0

        arr = [random.randint(1, max_num) for _ in range(arr_len)]
        return arr


def enter_list_manually() -> list:
        nums = input("\nEnter the array(each element divide by space)\n-> ").split(" ")
        arr = [int(num) for num in nums if num.isdigit()]
        return arr


def selection_sort(arr:list, arr_len:int) -> None:
    print(f"\nOriginal array: {arr}")

    for i in range(arr_len-1, -1, -1):
        idx_max = i

        for j in range(i, -1, -1):
            if arr[idx_max] < arr[j]:
                idx_max = j

        arr[i], arr[idx_max] = arr[idx_max], arr[i]
    
    print(f"\nSorted array: {arr}")



if __name__ == '__main__':
    try:
        os.system('clear')
        print('Selection Sort'.center(100, "="))

        while True:
            try:
                choice = int(input("\nEnter array manually (0) or generate (1):\n-> "))
                if choice == 0:
                    arr = enter_list_manually()
                    break
                elif choice == 1:
                    arr = generate_random_list()
                    break
                else:
                    print('Invalid choice. Enter 0 or 1')
            except ValueError:
                print("Invalid input. Enter 0 or 1")

        selection_sort(arr, len(arr))
    
    except KeyboardInterrupt:
        os.system('clear')
        print("Close program...")