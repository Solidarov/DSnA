import os
from array_queue import ArrayQueue
from linked_list_queue import LinkedListQueue

class UserInterface:
    def __init__(self):
        self.queues = {}
        self.options = ['create', 'exit', 'saved']

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _exit(self):
        self._clear_screen()
        print("\nExit program")
        exit()
    
    def _check_saved_queues(self):
        if not self.queues:
            msg = "\nNo queues available"
        else:
            msg = "\nAll available queues: "
            for key in self.queues:
                msg += f"\n\t{key}"
        return msg

    def _get_user_input_str(self, msg):
        while True:
            try:  
                user_choice = input(msg).lower().strip()
                break
            except ValueError:
                print("Please, provide the valid option")
            except:
                print("Something went wrong. Please try again")
        return user_choice

    def _get_user_input_int(self, msg):
        while True:
            try:  
                user_choice = int(input(msg).lower().strip())
                break
            except ValueError:
                print("Please, provide the valid option")
            except:
                print("Something went wrong. Please try again")
        return user_choice

    def _create(self):
        msg = "\nEnter the name of your queue -> "
        q_name = self._get_user_input_str(msg)

        msg = "\nEnter the size of your queue -> "
        q_size = self._get_user_input_int(msg)

        msg = "\nEnter based on what you want your queue"
        msg += "\nArray(array) or Linked List (list) -> "
        q_type = self._get_user_input_str(msg)

        if q_type == 'array':
            self.queues[q_name] = ArrayQueue(q_size)
        elif q_type == 'list':
            self.queues[q_name] = LinkedListQueue(q_size)
        else:
            return "\nSomething went wrong. Please try again"
        
        msg = f"\nQueue {q_name} based on {q_type} was successfully created"
        self.options.extend(['enqueue', 'dequeue', 'peek', 'display', 'delete'])
        return msg

    def _delete(self):
        msg = "\nEnter the name of the queue -> "
        q_name = self._get_user_input_str(msg)
        
        if q_name not in self.queues:
            msg = "\nNot found. Please, try again"
            return msg
        
        del self.queues[q_name]

        if not self.queues:
            self.options = ['create', 'exit', 'saved']
        
        msg = f"\nQueue {q_name} was deleted successfully"
        return msg

    def _enqueue(self):
        msg = "\nEnter the name of the queue -> "
        q_name = self._get_user_input_str(msg)
        
        if q_name not in self.queues:
            msg = "\nNot found. Please, try again"
            return msg
        
        msg = "\nEnter the value -> "
        q_value = self._get_user_input_int(msg)
        q_value = self.queues[q_name].enqueue(q_value)
        
        if q_value is not None:
            msg = f"\nValue {q_value} was successfully inserted into the {q_name} queue"
        else:
            msg = "\nSomething went wrong"

        return msg

    def _dequeue(self):
        msg = "\nEnter the name of the queue -> "
        q_name = self._get_user_input_str(msg)

        if q_name not in self.queues:
            msg = "\nNot found. Please, try again"
            return msg
        
        q_value = self.queues[q_name].dedequeue()

        if q_value is not None:
            msg = f"\nValue {q_value} was successfully poped from the {q_name} queue"
        else:
            msg = "\nSomething went wrong"
            
        return msg

    def _peek(self):
        msg = "\nEnter the name of the queue -> "
        q_name = self._get_user_input_str(msg)

        if q_name not in self.queues:
            msg = "\nNot found. Please, try again"
            return msg
        
        q_value = self.queues[q_name].peek()

        if q_value is not None:
            msg = f"\nThe first element of the queue {q_name} is {q_value}"
        else:
            msg = "\nSomething went wrong"
        
        return msg

    def _display(self):
        msg = "\nEnter the name of the queue -> "
        q_name = self._get_user_input_str(msg)

        if q_name not in self.queues:
            msg = "\nNot found. Please, try again"
            return msg
        
        msg = self.queues[q_name].display()
        if msg is None:
            msg = "\nSomething went wrong"
        return msg
    
    def run(self):
        self._clear_screen()
        print("Queue maker\n")

        while True:
            try:
                
                msg = "\nAvailable options: " + str(", ".join(self.options))
                msg += "\nEnter the options -> "
                
                user_choice = self._get_user_input_str(msg)
                
                if user_choice not in self.options:
                    raise ValueError

                if user_choice == 'exit':
                    self._exit()

                elif user_choice == 'saved':
                    msg = self._check_saved_queues()

                elif user_choice == 'create':
                    msg = self._create()

                elif user_choice == 'enqueue':
                    msg = self._enqueue()

                elif user_choice == 'dequeue':
                    msg = self._dequeue()

                elif user_choice == 'display':
                    msg = self._display()
                
                elif user_choice == 'peek':
                    msg = self._peek()

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