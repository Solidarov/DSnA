import random
#random.seed(42)

def generate_random_array() -> list:
        max_num = input("\nEnter the max number that array can contain:\n-> ")
        max_num = int(max_num) if max_num.isdigit() else 0

        arr_len = input("\nEnter the length of the array:\n-> ")
        arr_len = int(arr_len) if arr_len.isdigit() else 0

        arr = [random.randint(1, max_num) for _ in range(arr_len)]
        return arr

def manually_generate_array() -> list:
        nums = input("\nEnter the array(each element divide by space)\n-> ").split(" ")
        arr = [int(num) for num in nums if num.isdigit()]
        return arr