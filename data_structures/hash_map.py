import random
import string

class HashMap:
    def __init__(self, elements=[], capacity=10): #elementos = []      
        self.__size = 0
        self.__capacity = 10
        
        if not elements:
            self.__capacity = capacity
            self.__buckets = [[] for _ in range(self.__capacity)]
        else:
            self.__capacity = len(elements) * 2
            self.__buckets = [[] for _ in range(self.__capacity)]
            for k, v in elements:
                self.put(k,v)
        
    def put(self, key, value):
        bucket_index = self.__hash(key)
        bucket = self.__buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k==key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.__size += 1
        
        if self.__size / self.__capacity > 0.7:
            self.__resize()
            
    def get(self, key):
        value = self.__get(key)
        
        if value:
            return value
        return None
        #raise KeyError(f"key'{key}' not found")
        
    def __get(self, key):
        bucket_index = self.__hash(key)
        bucket = self.__buckets[bucket_index]
        
        for k, v in bucket:
            if k==key:
                return v
        
        return None
        
    def remove(self, key):
        bucket_index = self.__hash(key)
        bucket = self.__buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k==key:
                del bucket[i] # bucket.pop(i)
                self.__size -= 1
                return
            
        raise KeyError(f"key'{key}' not found")
    
    def __hash(self, key, base=None):
        if not base:
            base = self.__capacity
        
        return hash(key) % base
    
    def __resize(self):
        new_capacity = self.__capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        
        for bucket in self.__buckets:
            for k, v in bucket:
                new_bucket_index = self.__hash(k, new_capacity)
                new_buckets[new_bucket_index].append((k, v))
                
        self.__capacity = new_capacity
        self.__buckets = new_buckets
    
    def __repr__(self):
        elements = [f"{k}: {v}" if not isinstance(v, str) else f"{k}: '{v}'"
                    for bucket in self.__buckets for k, v in bucket]
        
        return "{" + ", ".join(elements)+"}"
    
    def keys(self):
        keys = []
        for bucket in self.__buckets:
            for k, v in bucket:
                keys.append(k)
                
        return keys
    
    def values(self):
        values = []
        for bucket in self.__buckets:
            for k, v in bucket:
                values.append(v)
                
        return values
    
    def items(self):
        items = []
        for bucket in self.__buckets:
            for k, v in bucket:
                items.append((k, v))
                
        return items
    
    def __len__(self):
        return self.__size
    
    def clear(self):
        self.__capacity = 10
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]
        
    def __contains(self, key):
        return True if self.__get(key) else False
    
    def __iter__(self):
        for bucket in self.__buckets:
            for k , v in bucket:
                yield k , v