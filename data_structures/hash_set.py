
class HashSet:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]
        
    def add(self, element)    :
        bucket_index = self.__hash(element)
        bucket = self.__buckets[bucket_index]
        
        if element not in bucket:
            bucket.append(element)
            self.__size += 1
            
        if self.__size / self.__capacity > 0.7:
            self.__resize()
            
    def remove(self, element):
        bucket_index = self.__hash(element)
        bucket = self.__buckets[bucket_index]
        
        if element in bucket:
            bucket.remove(element)
            self.__size -= 1
        else:
            raise KeyError(f"element '{element}' not found")   
        
    def __hash(self, element, base=None):
        if not base:
            base = self.__capacity
        
        return hash(element) % base
    
    def __resize(self):
        new_capacity = self.__capacity * 2
        new_buckets = [[] for _ in range((new_capacity))]
        
        for bucket in self.__buckets:
            for element in bucket:
                new_bucket_index = self.__hash(element, new_capacity)
                new_buckets[new_bucket_index].append(element)
                
        self.__capacity = new_capacity
        self.__buckets = new_buckets
    
    def __contains__(self, element):
        bucket_index = self.__hash(element)    
        bucket = self.__buckets[bucket_index]
        return True if element in bucket else False
    
    def __iter__(self):
        for bucket in self.__buckets:
            for element in bucket:
                yield element
    
    def __len__(self):
        return self.__size
    
    """ Operaciones de Conjuntos """
    def union(self, set2):
        new_set = HashSet()
        
        for element in set2:
            new_set.add(element)
        
        for element in self:
            new_set.add(element)
            
        return new_set
    
    def intersection(self, set2):
        new_set = HashSet()
        
        for element in self:
            if element in set2:
                new_set.add(element)
                
        return new_set
    
    def difference(self, set2):
        new_set = HashSet()
        
        for element in set2:
            if element not in self:
                new_set.add(element)
                
        return new_set
    
    def symmetric_difference(self, set2):
        new_set = HashSet()
        
        for element in set2:
            if element not in self:
                new_set.add(element)
            
        for element in self:
            if element not in set2:
                new_set.add(element)
                
        return new_set
    
    def __or__(self, set2):
        return self.union(set2)
    
    def __and__(self, set2):
        return self.intersection(set2)
    
    def __xor__(self, set2):
        return self.symmetric_difference(set2)
    
    def __repr__(self):
        elements = [f"{element}" if not isinstance(element, str) else f"'{element}'" 
                    for bucket in self.__buckets for element in bucket]
        
        return "{" + ", ".join(elements) + "}"