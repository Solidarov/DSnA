import os
from linked_list import SingleLinkedList, DoubleLinkedList

class UserInterface:
    def __init__(self):
        self.options = ['create', "exit"]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _exit(self):
        self.clear_screen()
        print("\nExit program")
        exit()

    def _create_linked_list(self):
        while True:
            try:
                msg = "\nWhich type of linked list, you want to create"
                msg += "\n(single) or (double) -> "
                list_type = input(msg).lower().strip()
                if list_type == 'single':
                    linkedlist = SingleLinkedList()
                elif list_type == 'double':
                    linkedlist = DoubleLinkedList()
                else:
                    raise ValueError
                
                self.options.extend(["insert", "search", "delete", "display"])
                self.options.remove('create')
                return linkedlist
            
            except ValueError:
                print("Please, provide the correct value")
            except:
                print("Something went wrong. Please, try again")
    
    def _insert_value(self, linkedlist: SingleLinkedList|DoubleLinkedList):
        while True:
            try:
                value = input("\nEnter the value: ")
                if value.isdigit():
                    value = int(value)

                msg = "Which type of insertion, you want to use"
                msg += "\n(end) or (start) -> "
                insert_type = input(msg).lower().strip()

                if insert_type == 'end':
                    linkedlist.insert_at_end(value)
                elif insert_type == 'start':
                    linkedlist.insert_at_start(value)
                else:
                    raise ValueError

                print(f"Value {value} was successfully inserted at the {insert_type} of the list")
                return
            
            except ValueError:
                print("Please, provide the correct value")
            except:
                print("Something went wrong. Please, try again")
    
    def _search(self, linkedlist: SingleLinkedList|DoubleLinkedList):
        while True:
            try:
                data = input("\nEnter the searched data: ")
                if data.isdigit():
                    data = int(data)
                idx = linkedlist.search(data)

                if idx is not None:
                    print(f"Value {data} is on the index {idx}")
                elif idx is None:
                    print("Value not found")
                else:
                    raise Exception
                
                return

            except ValueError:
                print("Please, provide the correct value")
            except:
                print("Something went wrong. Please, try again")

    def _delete(self, linkedlist: SingleLinkedList|DoubleLinkedList):
        while True:
            try:
                msg = "\nWhich type of deletion you want"
                msg += "\n(all) or (index) -> "
                delete_type = input(msg).lower().strip()

                if delete_type == "all":
                    result = linkedlist.delete()

                elif delete_type == "index":
                    idx = int(input("Enter the index: "))
                    result = linkedlist.delete_at(idx)

                else:
                    raise ValueError
                
                if result and delete_type == "all":
                    print("Linked List was successfully deleted")
                    self.options = ['create', 'exit']

                elif result and delete_type == "index":
                    print(f"Value at index {idx} was successfully deleted")

                elif result is None:
                    print("Not found")

                else:
                    raise Exception
                
                return
            
            except ValueError:
                print("Please, provide the correct value")
            except:
                print("Something went wrong. Please, try again")

    def _display_list(self, linkedlist: SingleLinkedList|DoubleLinkedList):
        while True:
            try:
                msg = "\nHow do you want to display list"
                if isinstance(linkedlist, SingleLinkedList):
                    msg += "\n(forward) -> "
                elif isinstance(linkedlist, DoubleLinkedList):
                    msg += "\n(forward) or (backward) -> "
                
                display_type = input(msg).lower().strip()

                if display_type == "forward":
                    ll_structure = linkedlist.display_forward()
                
                elif display_type == "backward" and isinstance(linkedlist, DoubleLinkedList):
                    ll_structure = linkedlist.display_backward()
                
                else:
                    raise ValueError
                
                print(ll_structure)
                return

            except ValueError:
                print("Please, provide the correct value")
            except:
                print("Something went wrong. Please, try again")


    def run(self):
        self.clear_screen()
        print("Welcome to the linked list maker")
        while True:
            try:
                print("\nAvailable options:", ", ".join(self.options))
                
                user_choice = input("Enter the option: ").lower().strip()
                
                if user_choice not in self.options:
                    raise ValueError

                if user_choice == 'exit':
                    self._exit()

                elif user_choice == 'create':
                    self.linkedlist = self._create_linked_list()

                elif user_choice == 'insert':
                    self._insert_value(self.linkedlist)

                elif user_choice == 'search':
                    self._search(self.linkedlist)

                elif user_choice == 'delete':
                    self._delete(self.linkedlist)

                elif user_choice == 'display':
                    self._display_list(self.linkedlist)

                else:
                    raise ValueError
                
            except ValueError:
                print("\nPlease, provide the valid option")

            except KeyboardInterrupt:
                self.clear_screen()
                print("\nOperation cancelled")
                exit()

