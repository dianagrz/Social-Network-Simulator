class Node:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
class Heap:
    def __init__(self):
        self.__root = None
        self.__size = 0
        
    def enqueue(self, priority, data):
        new_node = Node(priority, data)
        
        if not self.__root:
            self.__root = new_node
        else:
            self.__insert_node(new_node)
            self.__bubble_up(new_node)
            
        self.__size += 1
    
    def __insert_node(self, new_node):
        path = bin(self.__size+1)[3:]
        current = self.__root
        parent = None
        
        for direction in path:
            parent = current
            current = current.left if direction == '0' else current.right
            
        new_node.parent = parent
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node 
            
    def dequeue(self):
        if not self.__root:
            raise IndexError("deque from empty queue")
            
        max_node = self.__root
        priority, data = max_node.priority, max_node.data
        
        if self.__size == 1:
            self.__root = None
        else:   
            last_node = self.__find_last_node()
            self.__swap(max_node, last_node)
            self.__remove_last_node()
            self.__bubble_down(self.__root)
            
        self.__size-=1
        
        return priority, data
            
    def __bubble_up(self, node):
        while node.parent:
            if node.parent.priority < node.priority:
                self.__swap(node.parent, node)
                node = node.parent
            else:
                break
            
    def __bubble_down(self, node):
        while node.left:
            bigger_child = node.left
            
            if node.right and node.right.priority > bigger_child.priority:
                bigger_child = node.right
                
            if node.priority < bigger_child.priority:
                self.__swap(node, bigger_child)
                node = bigger_child
            else:
                break
                
    def __swap(self, node1, node2):
        node1.priority, node2.priority = node2.priority, node1.priority
        node1.data, node2.data = node2.data, node1.data
        
    def __find_last_node(self):
        path = bin(self.__size)[3:]
        current = self.__root
        
        for direction in path:
            current = current.left if direction == '0' else current.right
        return current
    
    def __remove_last_node(self):
        path = bin(self.__size)[3:]
        current = self.__root
        parent = None
        
        for direction in path:
            parent = current
            current = current.left if direction =='0' else current.right
            
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
            
    def get_root(self):
        return self.__root
    
    def get_size(self):
        return self.__size
    
    def print_heap(self, node, n):
        if node:
            self.print_heap(node.left, n+1)
            print("       "*n + f"({node.priority}, {node.data}")
            self.print_heap(node.right, n+1)
            
##EJERCICIOS DE IMPLEMENTACION
            
    def __find_node(self, index):
        path = bin(index + 1)[3:]
        current = self.__root
        
        for direction in path:
            current = current.left if direction == '0' else current.right
            
        return current
    
    def __rearange(self):
        def heapify(node):
            if not node:
                return
            
            max_node = node
            if node.left and node.left.priority > node.priority:
                max_node = node.left
            if node.right and node.right.priority > node.priority:
                max_node = node.right
            if max_node != node:
                self.__swap(node, max_node)
        
        def recursion(node):  
            if not node:
                return
            recursion(node.left)
            recursion(node.right)
            
            heapify(node)
            
        recursion(self.__root)

    def change_priority(self, index, priority):
        node = self.__find_node(index)
        prev = node.priority
        node.priority = priority
        if prev < priority:
            self.__bubble_up(node)
        else:
            self.__bubble_down(node)
            
    def remove(self, index):
        node = self.__find_node(index)
        last_node = self.__find_last_node()
        
        self.__swap(last_node, node)
        self.__remove_last_node() 
        self.__rearange()
    
    def __toss(self, node_list):
        for node in node_list:
            self.__insert_node(node)
    
    def insert_list(self, node_list):
        self.__toss(node_list)
        self.__rearange()
    
    def convert_to_min_heap(self):
        def heapify(node):
            if not node:
                return
            
            min_node = node
            if node.left and node.left.priority < node.priority:
                min_node = node.left
            if node.right and node.right. priority < node.priority:
                min_node = node.right
            if min_node != node:
                self.__swap(min_node, node)
                heapify(min_node)
        
        def recursion(node):
            if not node:
                return
            
            recursion(node.left)
            recursion(node.right)
            heapify(node)
            
        recursion(self.__root)
    
    def print_top_k(self, k):
        top_k = []
        q = []
        
        q.append(self.__root)
        counter = 0
        while len(q) > 0 and counter < k:
            node = q.pop(0)
            top_k.append(node)
            counter += 1
            for i in (node.left, node.right):
                if i and not (i in top_k):
                    q.append(i)
                    
        for i in top_k:
            print(f'({i.priority}, {i.data}), ')
        print()
    
    def is_valid_heap(self):
        is_max = None
        
        q = []
        visited = set()
        q.append(self.__root)
        while not len(q) == 1:
            node = q.pop(0)
            visited.add(node)
            for i in (node.left, node.right):
                if is_max == None and node.priority != i.priority:
                    is_max =  True if node.priority > i.priority else False
                elif is_max and i.priority > node.pririty:
                    return False
                elif is_max == False and i.priority < node.priority:
                    return False
                q.append(i)
        return True
        
def merge_recursivo(heap_1, heap_2):
    root = heap_2.get_root()
    
    def recursive_add(node):
        if not node:
            return
        
        heap_1.enqueue(node.priority, node.data)
        if node.left:
            recursive_add(node.left)
            if node.right:
                recursive_add(node.right)
                
    recursive_add(root)

    
def merge_iterativo_1(heap_1, heap_2):
    root = heap_2.get_root()
    q = []
    visited = set()
    q.append(root)
    while len(q) > 0:
        node = q.pop(0)
        visited.add(node)
        heap_1.enqueue(node.priority, node.data)
        for i in (node.left, node.right):
            if i and not (i in visited):
                q.append(i)
    
def merge_iterativo_2(heap_1, heap_2):
    while heap_2.get_size() > 0:
        priority, data = heap_2.dequeue()
        heap_1.enqueue(priority, data)
    
def merge_multiple_heaps(lista):
    main_heap = lista.pop(0)
    
    def merge(heap_1, heap_2):
        while heap_2.get_size() > 0:
            priority, data = heap_2.dequeue()
            heap_1.enqueue(priority, data)
    
    for heap in lista:
        merge(main_heap, heap)