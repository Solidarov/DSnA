import os
from graph import UndirectedGraph

class UserInterface:
    def __init__(self):
        self.graphs = {}
        self.options = ['exit', 'create', 'saved']


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
                
                if u_type == "s":
                    return user_choice
                
                elif u_type == "i":
                    return int(user_choice) if user_choice else 0
                
                elif u_type == "l":
                    return list(user_choice.split())
                
                else:
                    raise Exception
                
            except ValueError:
                print("Please, provide the valid option")
            except:
                print("Something went wrong. Please try again")
    

    def _create_graph(self):
        msg = "Enter the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name in self.graphs or not graph_name:
            print(f"Please, provide the valid name of the graph")
            return

        msg = "Enter the name of vertices, separate by space -> "
        vertices = self._get_user_input(msg, 'l')
        self.graphs[graph_name] = UndirectedGraph(vertices)

        opt = ['dfs', 'bfs', 'kruskal', 'prim','add_edge', 'del_edge', 'display', 'del_graph']

        if not any(o in self.options for o in opt):
            self.options.extend(opt)

    def _delete_graph(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        del self.graphs[graph_name]
        
        if not self.graphs:
            opt_remove = ['dfs', 'bfs', 'kruskal', 'prim','add_edge', 'del_edge', 'display', 'del_graph']
            self.options = [opt for opt in self.options if opt not in opt_remove]

        print(f"{graph_name} was successfully deleted")

    def _check_graph(self):
        if not self.graphs:
            msg = "\nNo graph available"
        else:
            msg = "\nAll available grahp: "
            for key in self.graphs:
                msg += f"\n\t{key}"
        print(msg)

    def _add_edges(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        while True:
            msg = "\nEnter the start vertice (type 'q' to quit) -> "
            start_ver = self._get_user_input(msg, 's')

            if start_ver == 'q': 
                break

            msg = "Enter the end vertice -> "
            end_ver = self._get_user_input(msg, 's')

            if end_ver == 'q':
                break
            
            msg = "Enter the weight (optional) -> "
            weight = self._get_user_input(msg, 'i')

            if weight == 'q':
                break

            if self.graphs[graph_name].add_edge(start_ver, end_ver, weight):
                print(f"{start_ver} and {end_ver} was successfully connected")

            elif not self.graphs[graph_name].add_edge(start_ver, end_ver):
                print(f"Vertex {start_ver} or {end_ver} does not exist. Please, try again")
            
            else:
                print(f"Something went wrong. Please, try again")


    def _del_edges(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        while True:
            msg = "Enter the start vertice (type 'q' to quit) -> "
            start_ver = self._get_user_input(msg, 's')

            if start_ver == 'q': 
                break

            msg = "Enter the end vertice -> "
            end_ver = self._get_user_input(msg, 's')

            if end_ver == 'q':
                break

            if self.graphs[graph_name].del_edge(start_ver, end_ver):
                print(f"{start_ver} and {end_ver} was successfully disconnected")

            elif not self.graphs[graph_name].del_edge(start_ver, end_ver):
                print(f"Vertex {start_ver} and {end_ver} does not exist. Please, try again")
            
            else: 
                print(f"Something went wrong. Please, try again")
    
    def _dfs(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        msg = "Enter the starting vertice -> "
        start_ver = self._get_user_input(msg, 's')
        
        if start_ver not in self.graphs[graph_name].vertices:
            print(f"{start_ver} does not exit. Please, try again")

        dfs_path = self.graphs[graph_name].dfs(start_ver)

        msg = f"Result of Deep First Search for graph {graph_name}\n"
        print(msg, dfs_path)

    def _bfs(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        msg = "Enter the starting vertice -> "
        start_ver = self._get_user_input(msg, 's')
        
        if start_ver not in self.graphs[graph_name].vertices:
            print(f"{start_ver} does not exit. Please, try again")

        bfs_path = self.graphs[graph_name].bfs(start_ver)

        msg = f"Result of Deep First Search for graph {graph_name}\n"
        print(msg, bfs_path)

    def _kruskal(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        msg = f"Result of the Kruskal Algorithm for graph {graph_name}"
        print(msg)
        self.graphs[graph_name].kruskal()

    def _prim(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        msg = "Enter the starting vertice -> "
        start_ver = self._get_user_input(msg, 's')
        
        if start_ver not in self.graphs[graph_name].vertices:
            start_ver = None

        msg = f"Result of the Prim Algorithm for graph {graph_name}"
        print(msg)
        self.graphs[graph_name].prim(start_ver)
        

    def _display_graph(self):
        msg = "Choose the name of the graph -> "
        graph_name = self._get_user_input(msg, 's')

        if graph_name not in self.graphs.keys():
            print(f"{graph_name} doesnt exist. Please try again")
            return
        
        self.graphs[graph_name].visualize()


    def run(self):
        self._clear_screen()
        print("Graph maker\n")

        while True:
            try:
                
                msg = "\nAvailable options: " + str(", ".join(self.options))
                msg += "\nEnter the options -> "
                
                user_choice = self._get_user_input(msg, 's')
                
                if user_choice not in self.options:
                    raise ValueError

                if user_choice == 'exit':
                    self._exit()

                elif user_choice == 'saved':
                    self._check_graph()

                elif user_choice == 'create':
                    self._create_graph()

                elif user_choice == 'add_edge':
                    self._add_edges()

                elif user_choice == 'del_edge':
                    self._del_edges()

                elif user_choice == 'del_graph':
                    self._delete_graph()

                elif user_choice == 'dfs':
                    self._dfs()

                elif user_choice == 'bfs':
                    self._bfs()
                
                elif user_choice == 'kruskal':
                    self._kruskal()

                elif user_choice == 'prim':
                    self._prim()

                elif user_choice == 'display':
                    self._display_graph()

                else:
                    raise ValueError
                
            except ValueError:
                print("\nPlease, provide the valid option")

            except KeyboardInterrupt:
                self._clear_screen()
                print("\nOperation cancelled")
                exit()