import os
from hashmap import Hashmap

class UserInterface:

    def __init__(self):
        self.available_opt = ["create", "exit"]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _create_hasmap(self):
        while True:
            try:
                size = int(input("Enter the size of hash table: "))
                hashmap = Hashmap(size)
                self.available_opt.extend(['set', 'find', 'del', 'show'])
                self.available_opt.remove('create')
                return hashmap
            except ValueError:
                print("\nPlease, provide the number")

    def _set_the_value(self, hashmap):
        while True:
            try:
                key = input("Enter the key: ")
                val = input("Enter the value: ")
                if key.isdigit():
                    key = int(key)
                if val.isdigit():
                    val = int(val)
                hashmap.set_val(key, val)
                print(f"{key}: {val} successfully set")
                return
            except ValueError:
                print("\nPlease provide number or text")

    def _find_by_key(self, hasmap:Hashmap):
        while True:
            try:
                key = input("Enter the key: ")
                if key.isdigit():
                    key = int(key)
                result = hasmap.find_val(key)
                print(f"The value for the key \"{key}\": {result}")
                return
            except ValueError:
                print("\nPlease provide number or text")

    def _delete_by_key(self, hasmap:Hashmap):
        while True:
            try:
                key = input("Enter the key: ")
                if key.isdigit():
                    key = int(key)
                result = hasmap.del_val(key)
                if result:
                    print("\nSuccessfully deleted")
                else:
                    print("\nKey not found")
                return
            except ValueError:
                print("\nPlease provide number or text")

    def _show_hashtable(self, hashmap: Hashmap):
        result = hashmap.show_table()
        print(result)

    def _exit(self):
        self.clear_screen()
        print("\nExit program")
        exit()

    def run(self):
        self.clear_screen()
        while True:
            try:
                print("\nAvailable options:", ', '.join(self.available_opt))
                user_choice = input("Enter the option: ").lower()
                if user_choice not in self.available_opt:
                    print("\nPlease, provide the valid option")
                    continue
                if user_choice == 'exit':
                    self._exit()

                elif user_choice == 'create':
                    self.hashmap = self._create_hasmap()

                elif user_choice == 'set':
                    self._set_the_value(self.hashmap)

                elif user_choice == 'find':
                    self._find_by_key(self.hashmap)

                elif user_choice == 'del':
                    self._delete_by_key(self.hashmap)

                elif user_choice == 'show':
                    self._show_hashtable(self.hashmap)

                else:
                    print("\nPlease, provide the valid option")

            except KeyboardInterrupt:
                self.clear_screen()
                print("\nOperation cancelled")
                exit()