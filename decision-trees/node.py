
class Node:
    
    id_class = 0

    def __init__(self, class_name, n_elements, branches):
        if type(branches) != list:
            raise TypeError("Branches should be a list")

        self._class_name = class_name
        self._number_of_elements = n_elements
        self._branches = branches
        self._id = Node.id_class
        Node.id_class = Node.id_class + 1

    def get_nodes(self):
        return self.branches

    def get_elements(self):
        return self.number_of_elements

    def get_class(self):
        return self._class_name

    def set_nodes(self, branches):
        self.branches = branches

    def set_elements(self, n_elements):
        self.number_of_elements = n_elements

    def set_class(self, class_name):
        self._class_name
        
    #branches is a list of nodes

    '''
    ---------------
    |
    |   Number of elements
    |
    |   branches
    |
    ---------------
    '''
    # nodo1:
    # categorias restantes
    #     nodo2:
    #     categorias restantes
    #         nodo3:
    #         categorias restantes
    #             nodo4:
    #             categorias restantes
    # [---|---|---|---TOTAL-----------]
    # [---|---|---|---TOTAL-----------]
    # [---|---|---|---TOTAL-----------]
    # [---|---|---|---TOTAL-----------]
    # [---|---|---|---TOTAL-----------]
    # [---|---|---|---TOTAL-----------]
