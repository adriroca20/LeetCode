
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        prev_last = self.head
        while prev_last.next is not self.tail :
            prev_last = prev_last.next
        prev_last.next = None
        temp = self.tail
        self.tail = prev_last
        self.length -=1
        return temp
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        self.head = self.head.next
        return temp
    def get(self, index):
        temp = self.head
        for i in range(index):
            if(temp.next == None):
                return None
            temp = temp.next
        return temp

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
test = my_linked_list.get(3)
my_linked_list.printList()  # 5
print("Get value", test.value)
