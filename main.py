class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def putHerOnTheBack(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def howManyInThere(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def showMeThat(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def getThatShit(self,index):
        if index >= self.howManyInThere():
            print("ERROR 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self,index):
        if index >= self.howManyInThere():
            print("ERROR: 'Erase' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1



my_list = linked_list()
# my_list.display() #
my_list.showMeThat()
# my_list.append() #
my_list.putHerOnTheBack(1)
my_list.putHerOnTheBack(2)
my_list.putHerOnTheBack(3)
my_list.putHerOnTheBack(4)
# my_list.display() #
my_list.showMeThat()
# print(my_list.get(1))
print("Here's your data: {}".format(my_list.getThatShit(2)))
my_list.erase(1)
my_list.showMeThat()
