class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data) 
       
        if not self.head:
            self.head = new_node
            return
       
        current = self.head
        if not current.next:
            current.next = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node
            
    def insert_index_init(self, data, index=0):
        if index<0 or not isinstance(index, int):
            raise ValueError("Index must be real positive int")
        current = self.head
        last = None
        counter = 0
        
        while current and counter<index:
            last = current
            current = current.next
            counter += 1
        new_node = Node(data)
        
        if not current and counter != index:
            raise ValueError("Index out of limits")
        if not last:
            new_node.next = self.head
            self.head = new_node
            return 
        
        new_node.next = current
        last.next = new_node
    
    def length(self):
        current = self.head
        length = 0
        
        while current:
            current = current.next
            length +=1
            
        return length
            
    def index(self, value):
        if not self.head:
            return
        
        current = self.head
        counter = 0
        
        while current:
            if current.data == value:
                    print("Indice ", counter)
            current = current.next
            counter += 1
        
        if not current:
            return
    
    def remove_value(self, value):
        if not self.head:
            return
        
        current = self.head
        last = None
        
        while current and current.data != value:
            last = current
            current = current.next
        
        if not last:
            self.head= current.next
            return
        
        last.next = current.next
    
    def remove_index(self, indice):
        if not self.head:
            return
        current = self.head
        count = 0
        
        if indice == 0:
            self.head=current.next
            return
        
        while current and count<indice:
            last = current
            current = current.next
            count += 1
        
        last.next = current.next
            
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = ", ")
            current = current.next
        print()
        
    def reverse(self):
        curr = self.head
        prev = None
        
        while curr:
            sig = curr.next
            curr.next = prev
            prev = curr
            curr = sig
        self.head = prev

    def sort(self, order=False):
        end = None
        while end != self.head:
            current = self.head
            while current.next != end:
                sig = current.next
                if ((order == False and current.data > sig.data) or (order == True and current.data < sig.data)):
                    current.data, sig.data = sig.data, current.data
                current = sig
            end = current

    def sort_punteros(self, descendent = False):
        if not self.head:
            return

        sorting = True
        while sorting:
            sorting = False
            current = self.head
            last = None

            while current and current.next:
                if ((not descendent and current.data > current.next.data) 
                    or (descendent and current.data < current.next.data)):
                    sorting = True
                    if last is None:
                        self.head = current.next
                    else:
                        last.next = current.next
                        
                    temp = current.next
                    current.next = current.next.next
                    temp.next = current
                    last = temp

                    if not last:
                        last = self.head
                    else:
                        last = last.next
                else:
                    last = current
                    current = current.next
                    
    def copy(self):
        nuevaLista = LinkedList()
        current = self.head
        
        while current:
            nuevaLista.append(current.data)
            current = current.next
            
        return nuevaLista

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    def merge(self, lista):
        current = self.head
        
        while current.next:
            current = current.next
        current.next = lista.head
    
    def deleteDuplicates(self):
        current = self.head
        unicos = set({})
        while current:
            if (current.data in unicos):
                self.remove_value(current.data)
            else: 
                unicos.add(current.data)
            current = current.next

    def nToLast(self, n):
        curr = self.head
        for i in range(self.length() - n):
            curr = curr.next
            
        return curr.data