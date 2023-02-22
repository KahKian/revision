# Linked List Class

class Node:
    def __init__(self, value):
        # create a linkedlist node with data and next pointer
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        # initialise a linked list with head as none
        self.head = None



    def insertAtHead(self, node):
        if self.head is None:
            # For insert, if the list is empty (head is none), assign node to head
            self.head = node
        else:
            # else, assign current head to next and new node to head
            node.next = self.head
            self.head = node

    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.data is value:
                return temp
            temp = temp.next
        print("not found")

    def print(self):
        temp = self.head
        print("Current list content: ")
        while temp is not None:
            print('[ '+temp.data+' ]')
            temp = temp.next

    def remove(self, value):
        # create temp and point to head
        # create a prev and point to None as we are still at start of the list
        temp = self.head
        prev = None
        # while we are not at the end of the list
        while temp is not None:
            # if temp is not the value we want to delete
            # prev will be current node (temp) and temp will become the next node
            if temp is not value:
                prev = temp
                temp = temp.next
            # else if value found
            # assign prev node's next to current node's (temp) next
            # then delete current node
            else:
                prev.next = temp.next
                del temp

list = LinkedList()
node = Node('2')
node2 = Node('3')
node3 = Node('7')
list.insertAtHead(node)
list.insertAtHead(node2)
list.insertAtHead(node3)
list.print()
print(list.search('3'))