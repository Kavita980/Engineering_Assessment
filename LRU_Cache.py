#Following code implementation demonstrate the "Least Recently Used (LRU)" cache
#Following class implemented for the doubly linked list (DLL) which represents the structure of the node
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)

#Following class is the construction of LRU
class LRUCache(object):
    #When LRUCache object initialize with the maximum size as the following constructor can be called
    def __init__(self,size):
        #size of the cache should be > 0
        if size <= 0:
            raise ValueError("Size of the cache should be > 0")
        
        #hash-map implemented to keep the track of the items stored into cache
        self.hash_map = {}

        #following are two pointers initialised with value none as the cache is empty
        self.head = None #pointer points to the latest added element in DLL
        self.end = None #pointer points to the last element in the DLL

        #following variable defines the maximum capicity and current size of the cache
        self.capacity = size
        self.current_size = 0

    #following function used to insert the value of a key pair into LRU cache
    def put(self, key, value):
        #if the key is already present into the hash-map the value of that key will be updated
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
        else:
            #otherwise new node will be created in DLL i.e. value of the key will be added to the cache
            new_node = Node(key,value)
            #but before that capacity of the LRU will be checked
            if self.current_size == self.capacity:
                #if Cache is full then Least Recently Used element (Last element) will be deleted
                del self.hash_map[self.end.key] #key is deleted from the hash-map
                self.remove(self.end) #last element will be removed from the cache
            #head pointer will point to the newly added element which is inserted at the front of DLL
            self.set_head(new_node)
            self.hash_map[key] = new_node

    #following function used to retrieve the value of the key
    def get(self,key) -> int:
        #first check that if the key is exist or not
        if key not in self.hash_map:
            print("key is not present into the cache")
            return -1
        
        #if key exist value will be retrieved in the form of node
        node = self.hash_map[key]

        #return the value if we are looking at the head
        if self.head == node:
            return node.value
        #otherwise that node will be removed from the original position
        #and inserted at the front as it is accessed recently
        #and head pointer will point to that node
        self.remove(node)
        self.set_head(node)
        #return the value of the key
        return node.value

    #following function used to delete the key
    def delete(self, key):
        if key not in self.hash_map:
            print("Attempting to delete the key which doesn't exist")
        
        #if key exist into teh hash-map then node will be retrievd
        node = self.hash_map[key]
        #if the node is head in our cache then following operation will be performed to delete it and head will be shifted to the next element
        if node == self.head:
            self.head = node.prev
            node.key = None
            node.value = None
            self.current_size -= 1
        
        #otherwise the remove function is called to delete the element if its in the middle of at the end
        else:
            self.remove(node)
            node.key = None
            node.value = None

    #following function used to reset the cache which removes all the items from teh LRU-Cache
    def reset(self):
        self.head = None
        self.end = None

    #following function used to update the head pointer if we insert or delete the element        
    def set_head(self,node):
        #if the cache is empty 
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1

    #following function used to remove the element if we insert the element after the LRU reaches to its maximum capacity
    def remove(self,node):
        #if the cache is empty
        if not self.head:
            return

        #if the removing node in the middle then update the pointers
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        #if the only one node in the cache i.e. head = end = node
        if not node.next and not node.prev:
            self.head = None
            self.end = None

        #if the node at the end then also update the pointer
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        
        self.current_size -= 1
        return node

    #following function used to print the data into cache
    def printCache(self):
        x = self.head
        print("[head = %s, end = %s]" %(self.head, self.end), end = " ")
        print("\n")
        while x:
            print("%s -> " % (x), end = "")
            x = x.prev
        print("Null")

#object of type LRUCache is initialised with the maximum capacity of 3
lruCache = LRUCache(3)

#following are the series of the functions which will be perfomed on the LRU Cache
lruCache.put(1,2)
lruCache.put(2,3)
lruCache.put(3,4)
lruCache.put(4,5)
lruCache.delete(3)
lruCache.put(5,6)
lruCache.get(2)
lruCache.put(6,7)
#Latest state of the LRU cache will be printed after the above all operations
lruCache.printCache()
lruCache.reset()
lruCache.printCache()