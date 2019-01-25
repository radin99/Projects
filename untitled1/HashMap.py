class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashmap:
    Empty = True
    size = 0
    KeyLists = []
    ValueLists = []
    GlobalLists = []
    def __init__(self):
        self.store = [None for _ in range(42)]

    def Get(self, key):
        if(self.Empty != True):
            index = hash(key) % 41
            if self.store[index] is None:
                return "We don't have this Key and Value"
            n = self.store[index]
            while True:
                if n.key == key:
                    return n.value
                else:
                    if n.next:
                        n = n.next
                    else:
                        return "We don't have this Key and Value"
        else:
            return "We don't have this Key and Value"

    def Put(self,key, value):
        self.Empty = False
        nd = Node(key, value)
        index = hash(key) % 41
        self.size = self.size + 1

        n = self.store[index]
        if n is None:
            self.store[index] = nd
        else:
            if n.key == key:
                n.value = value
                self.size = self.size - 1
            else:
                while n.next:
                    if n.key == key:
                        n.value = value
                        self.size = self.size - 1
                        return
                    else:
                        n = n.next
                n.next = nd

    def IsEmpty(self):
        if self.size == 0:
            return "It's Empty"
        else:
            return "It's not Empty"

    def ContainKey(self,key):
        index = hash(key) % 41
        n = self.store[index]
        if n is None:
            return "We don't have this Key"
        while True:
            if n.key == key:
                return "We have this Key!"
            else:
                if n.next:
                    n = n.next
                else:
                    return "We don't have this Key"

    def HashSize(self):
        return self.size

    def KeySet(self):
        self.KeyLists.clear()
        for item in self.store:
            n = item
            while n:
                self.KeyLists.append(n.key)
                n = n.next
        return self.KeyLists

    def ValueSet(self):
        self.ValueLists.clear()
        for item in self.store:
            n =item
            while n:
                self.ValueLists.append(n.value)
                n = n.next
        return self.ValueLists

    def ClearTable(self):
        self.Empty = True
        self.store.clear()

    def RemoveItem(self,key):
        index = hash(key) % 41
        n = self.store[index]
        if self.store[index] is None:
            return "It doesn't exist"
        if n.key == key:
            n = n.next
            self.store[index] = n
            self.size = self.size -1
            return "DONE!"
        else:
            while True:
                if n.next.key == key:
                    n.next = n.next.next
                    #self.store[index] = n
                    self.size = self.size - 1
                    return "DONE!"
                else:
                    if n.next:
                        n = n.next
                    else:
                        return "It doesn't exist"
    def EntrySet(self):
        self.GlobalLists.clear()
        for item in self.store:
            n = item
            while n:
                self.GlobalLists.append([n.key,n.value])
                n = n.next
        return self.GlobalLists
    def Clone(self):
        return self
    def __len__(self):
        return self.size












