import os
import re
from array_stack import ArrayStack
from linked_list_stack import LinkedListStack

class UserInterface:
    def __init__(self):
        self.options = ['create', 'exit']

    def _create(self):
        while True:
            try:  
                msg = "\nCreate stack based on"
                msg += "\nArray(array) or Linked List(list) -> "
                user_input = input(msg).lower().strip()

                if user_input == 'array':
                    self.stack = ArrayStack()
                    break
                elif user_input == 'list':
                    self.stack = LinkedListStack()
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please, provide the valid option")
            except:
                print("Something went wrong. Please try again")
        
        self.options.remove('create')
        self.options.extend(['push', 'pop', 'display', 'delete'])
        msg = f"\nStack based on {user_input} was created successfully"
        return msg
        
    
    def _push(self):
        pattern = r"^-?\d+\.\d+$"
        while True:
            try:    
                msg = "\nEnter the value (text or number) -> "
                user_value = input(msg).strip()

                if not user_value:
                    raise ValueError
                if re.match(pattern, user_value) is not None:
                    raise ValueError
                if user_value.isdigit():
                    user_value = int(user_value)
                if isinstance(user_value, (str, int)) and user_value:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid value. Please, provide text or numbers")
            except:
                print("Something went wrong. Please try again")

        self.stack.push(user_value)
        msg = f"\nValue {user_value} was successfully pushed into the stack"
        return msg


    def _pop(self):
        poped_value = self.stack.pop()
        if poped_value is None:
            msg = "\nNo value to pop"
        else:
            msg = f"\nPoped value: {poped_value}"
        return msg
    

    def _display(self):
        while True:
            try:
                msg = "\nWhat do you want to display"
                msg += "\nTop element(top) or Whole stack(all) -> "
                user_input = input(msg).lower().strip()

                if user_input == 'top':
                    data = self.stack.display_top()
                    if data is None:
                        msg = "\nNo top value"
                    else:
                        msg = f"\nTop value is {data}"
                    return msg
                elif user_input == 'all':
                    msg = "\nStack structure:\n"
                    msg += self.stack.display()
                    return msg
                else:
                    raise ValueError
            except ValueError:
                print("Please, provide the valid option")
            except:
                print("Something went wrong. Please try again")


    def _delete(self):
        del self.stack
        msg = "\nThe whole stack was deleted"
        self.options = ['create', 'exit']
        return msg

    def _exit(self):
        self._clear_screen()
        print("\nExit program")
        exit()

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        self._clear_screen()
        print("Stack maker\n")

        while True:
            try:
                print("\nAvailable options:", ", ".join(self.options))
                
                user_choice = input("Enter the option: ").lower().strip()
                
                if user_choice not in self.options:
                    raise ValueError

                if user_choice == 'exit':
                    self._exit()

                elif user_choice == 'create':
                    msg = self._create()

                elif user_choice == 'push':
                    msg = self._push()

                elif user_choice == 'pop':
                    msg = self._pop()

                elif user_choice == 'display':
                    msg = self._display()

                elif user_choice == 'delete':
                    msg = self._delete()

                else:
                    raise ValueError
                
                print(msg)
            except ValueError:
                print("\nPlease, provide the valid option")

            except KeyboardInterrupt:
                self._clear_screen()
                print("\nOperation cancelled")
                exit()