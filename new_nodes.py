class Node:
    def __init__(self,year,highlight):
        self.year = year
        self.highlight = highlight
        self.next = None

    def get_year(self):
        return self.year

    def get_highlight(self):
        return self.highlight

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    #insert at the front(head)
    def push(self,new_year,new_highlight):
        new_node = Node(new_year,new_highlight)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_year, new_highlight):
        if prev_node is None:
            print ("The given previous node must be in linked list")
            return
        new_node = Node(new_year,new_highlight)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # append at the end
    def append(self, new_year, new_highlight):
        new_node = Node(new_year,new_highlight)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print ("Year: %s, Highlight: %s"%(temp.year,temp.highlight))
            temp = temp.next



my_list = LinkedList()
my_list.append(7,"I turned seven")
my_list.push(3,"I started walking")
my_list.push(0,"I was born")

current_node = my_list.get_head()
age = int(input("insert your age: "))
current_age = 0
while current_age <= age:
    if current_age > current_node.get_year() and current_age < current_node.get_next().get_year():
        highlight = input("insert the highlight of year %s: "%(current_age))
        my_list.insertAfter(current_node, current_age, highlight)
        current_age += 1
    elif current_age > current_node.get_year() and current_age > current_node.get_next().get_year():
        current_node = current_node.get_next()
    elif current_age > current_node.get_year() and current_node.get_next() == None:
        highlight = input("insert the highlight of year %s: "%(current_age))
        my_list.append(current_age, highlight)
        current_age += 1
    else:
        current_age += 1


my_list.printList()
