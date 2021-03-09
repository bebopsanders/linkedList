class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            total += 1
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        return elems

    def get(self,index):
        if index >= self.length():
            print("ERROR 'Get' Index out of range!")
            return
        cur_node = self.head
        cur_idx = 0
        searching = True
        while searching:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
                searching = False
            cur_idx += 1

    def erase(self,index):
        if index >= self.length():
            print("ERROR 'Erase' Index out of range!")
            return
        cur_node = self.head
        cur_idx = 0
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


# creating an instance of the class linked_list named my_list
my_list = linked_list()
# creating a second instance of the class linked_list named your_list
your_list = linked_list()
# calling the append method on the instance of linked_list named my_list and passing it a string "Yeah baby yeah!!!"
my_list.append("Yeah baby yeah!!!")
# same thing as before but this time passing another linked_list (instance object of linked_list:)
my_list.append(your_list)
# calling the append method on the instance of linked_list named my_list and passing it a string "There's another linked list in here?!"
my_list.append("There's another linked list in here?!")
# because i am only returning the data in length() and display() i am using the print() to 'print' out the data of length() and display()
print(my_list.length())
print(my_list.display())
# testing get() Error message if index is out of range
print(my_list.get(5))
# testing erase() Error message if index is out of range
print(my_list.erase(5))
# calling the erase method on the instance object my_list and passing the int 2 that represents the index at which we shall erase node & data
my_list.erase(2)
# again because i am returning the data in display() i am using the print() function to print my_list.display() to the user
print(my_list.display())
