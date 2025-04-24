import os
import random
import shutil
from typing import (List,
                    )
from strategy_interfaces import (SortStrategy,
                                 SearchStrategy)


class ArrayGenerator:
    @staticmethod
    def generate_random(size: int) -> List[int]:
        return [random.randint(1, 100) for _ in range(size)]
    
    @staticmethod
    def manual_input(size:int = 0) -> List[int]:
        while True:
            try:
                nums = input("\nEnter numbers separated by spaces: ").split(" ")
                return [int(num) for num in nums if num.isdigit()][0:size]
            except ValueError:
                print("Invalid input. Please enter integers only.")




class UserInterface:
    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            width = shutil.get_terminal_size().columns
        except:
            width = 80

        logo=[
        " __    __    ___  _____  ____  ____  ____  _   _  __  __  ___",
        "  /__\  (  )  / __)(  _  )(  _ \(_  _)(_  _)( )_( )(  \/  )/ __) ",
        " /(__)\  )(__( (_-. )(_)(  )   / _)(_   )(   ) _ (  )    ( \__ \ ",
        "(__)(__)(____)\___/(_____)(_)\_)(____) (__) (_) (_)(_/\/\_)(___/ ",
        " __    _  _  ____",
        "  /__\  ( \( )(  _ \ ",
        " /(__)\  )  (  )(_) ) ",
        "(__)(__)(_)\_)(____/ ",
        "____    __   ____   __      ___  ____  ____  __  __  ___  ____  __  __  ____  ____  ___",
        "(  _ \  /__\ (_  _) /__\    / __)(_  _)(  _ \(  )(  )/ __)(_  _)(  )(  )(  _ \( ___)/ __) ",
        " )(_) )/(__)\  )(  /(__)\   \__ \  )(   )   / )(__)(( (__   )(   )(__)(  )   / )__) \__ \\",
        "(____/(__)(__)(__)(__)(__)  (___/ (__) (_)\_)(______)\___) (__) (______)(_)\_)(____)(___/",
        "\n\n\n",
        ]

        for line in logo:
            print(line.center(width))
    
    @staticmethod
    def get_user_choice_dict(msg: str, options: dict) -> str:
        msg = f"\n{msg}: {', '.join(options.keys())} \n\t--> "
        while True:
            try:
                choice = input(msg).strip().lower()
                if choice in options:
                    return choice
                print(f"Invalid choice")
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                exit()
    
    @staticmethod
    def get_user_choice_num(msg: str) -> int:
        msg = f"\n{msg}: \n\t--> "
        while True:
            try:
                choice = int(input(msg))
                return choice
            except ValueError:
                print("\nYou must provide number")
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                exit()
    
    @staticmethod
    def get_array_method() -> None:
        array_methods = {
            'auto-generate': ArrayGenerator.generate_random,
            'manually': ArrayGenerator.manual_input,
        }
        choice = UserInterface.get_user_choice_dict("How to create an array",
                                                    array_methods)
        
       
        size = UserInterface.get_user_choice_num("Enter the size of array")
        return array_methods[choice](size)

    @staticmethod
    def get_results(choice_factory: str, data: List[int], strategy: SearchStrategy | SortStrategy) -> None:
        print(f"\nOriginal array: {data}")

        if choice_factory == 'sort':
            strategy.sort(data)
            print("Sorted data:", data)
        
        elif choice_factory == 'search':
            search_num = UserInterface.get_user_choice_num("Enter the searched number")
            index = strategy.search(data, search_num)
            print(f"Element {search_num} found at index: {index}")