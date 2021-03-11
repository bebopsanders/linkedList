class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.root = node()

    def append(self,data):
        new_node = node(data)
        cur_node = self.root
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def length(self):
        cur_node = self.root
        total = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            total += 1
        return total

    def display(self):
        elements = []
        cur_node = self.root
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        return elements

    def get(self,index):
        if index < 0:
            print("ERROR 'NegativeIndexError' Working on negative indexing sorry about that!")
            return
        elif index > self.length():
            print("ERROR 'IndexRangeError' Index out of range!")
            return
        cur_node = self.root
        cur_indx = 0
        while True:
            cur_node = cur_node.next
            if cur_indx == index:
                return cur_node.data
            cur_indx += 1

    def erase(self,index):
        if index < 0:
            print("ERROR 'NegativeIndexError' Working on negative indexing sorry about that!")
            return
        elif index > self.length():
            print("ERROR 'IndexRangeError' Index out of range!")
            return
        cur_node = self.root
        cur_indx = 0
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if index == cur_indx:
                last_node.next = cur_node.next
                return
            cur_indx += 1

import time
num_nodes = 1000
t0 = time.time()
new_list = linked_list()
for i in range(num_nodes):
    new_list.append("Node: " + str(i))
print(new_list.length())
for i in range(400):
    new_list.erase(i)
print(new_list.length())
t1 = time.time()
print("Time: {}".format(str(t1-t0)))
print(new_list.display())
