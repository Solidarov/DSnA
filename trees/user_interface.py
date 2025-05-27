import os
from simple_tree import Tree

class UserInterface:
    def __init__(self):
        self.trees = {}
        self.options = ['create', 'exit', 'saved']


    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def _exit(self):
        self._clear_screen()
        print("\nExit program")
        exit()


    def _get_user_input(self, msg, u_type):
        while True:
            try:  
                user_choice = input(msg).lower().strip()
                
                if u_type == "str":
                    return user_choice
                
                elif u_type == "int":
                    return int(user_choice)
                
                else:
                    raise Exception
                
            except ValueError:
                print("Please, provide the valid option")
            except:
                print("Something went wrong. Please try again")
    

    def _create_tree(self):
        msg = "Enter the name of the tree -> "
        tree_name = self._get_user_input(msg, 'str')
        self.trees[tree_name] = Tree()
        
        opt = ['insert', 'search', 'delete', 'deltree', 'display']


        if not any(o in self.options for o in opt):
            self.options.extend(opt)


    def _insert_into_tree(self):
        msg = "Choose the name of the tree -> "
        tree_name = self._get_user_input(msg, 'str')

        if tree_name not in self.trees.keys():
            print(f"{tree_name} doesnt exist. Please try again")
            return
        
        msg = "Enter the value -> "
        value = self._get_user_input(msg, 'int')

        if self.trees[tree_name].insert(value):
            print(f"{value} was successfully inserted into {tree_name}")

        elif not self.trees[tree_name].insert(value):
            print(f"{tree_name} already have value {value}. \nCannot insert the same value twice")
        else: 
            print(f"Something went wrong. Please, try again")


    def _search(self):
        msg = "Choose the name of the tree -> "
        tree_name = self._get_user_input(msg, 'str')

        if tree_name not in self.trees.keys():
            print(f"{tree_name} doesnt exist. Please try again")
            return
        
        msg = "Enter the searched value -> "
        value = self._get_user_input(msg, 'int')

        if self.trees[tree_name].search(value):
            print(f"{value} exist in the {tree_name}")

        else:
            print(f"{value} does not exist in the {tree_name}")

    
    def _delete(self):
        msg = "Choose the name of the tree -> "
        tree_name = self._get_user_input(msg, 'str')

        if tree_name not in self.trees.keys():
            print(f"{tree_name} doesnt exist. Please try again")
            return
        
        msg = "Enter the value to delete -> "
        value = self._get_user_input(msg, 'int')

        self.trees[tree_name].delete(value)
        print(f"{value} was successfully deleted from the {tree_name}")
        return
    
    def _delete_tree(self):
        msg = "Choose the name of the tree -> "
        tree_name = self._get_user_input(msg, 'str')

        if tree_name not in self.trees.keys():
            print(f"{tree_name} doesnt exist. Please try again")
            return
        
        del self.trees[tree_name]
        
        if not self.trees:
            opt_remove = ['insert', 'search', 'delete', 'deltree', 'display']
            self.options = [opt for opt in self.options if opt not in opt_remove]

        print(f"{tree_name} was successfully deleted")


    def _display_tree(self):
        msg = "Choose the name of the tree -> "
        tree_name = self._get_user_input(msg, 'str')

        if tree_name not in self.trees.keys():
            print(f"{tree_name} doesnt exist. Please try again")
            return
        
        tree_list = self.trees[tree_name].display()

        msg = f"Content of the tree {tree_name}\n"
        msg += "\t-> "
        print(msg, tree_list)

    def _check_tree(self):
        if not self.trees:
            msg = "\nNo trees available"
        else:
            msg = "\nAll available trees: "
            for key in self.trees:
                msg += f"\n\t{key}"
        print(msg)

    def run(self):
        self._clear_screen()
        print("Tree maker\n")

        while True:
            try:
                
                msg = "\nAvailable options: " + str(", ".join(self.options))
                msg += "\nEnter the options -> "
                
                user_choice = self._get_user_input(msg, 'str')
                
                if user_choice not in self.options:
                    raise ValueError

                if user_choice == 'exit':
                    self._exit()

                elif user_choice == 'saved':
                    self._check_tree()

                elif user_choice == 'create':
                    self._create_tree()

                elif user_choice == 'insert':
                    self._insert_into_tree()

                elif user_choice == 'search':
                    self._search()

                elif user_choice == 'delete':
                    self._delete()

                elif user_choice == 'deltree':
                    self._delete_tree()
                
                
                elif user_choice == 'display':
                    self._display_tree()


                else:
                    raise ValueError
                
            except ValueError:
                print("\nPlease, provide the valid option")

            except KeyboardInterrupt:
                self._clear_screen()
                print("\nOperation cancelled")
                exit()