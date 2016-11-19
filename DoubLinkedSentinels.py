__author__ = 'Sanket Agarwal'
class node:
    __slot__='data','prev','next'

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    __slot__ = 'head','tail'

    def __init__(self):
        self.head = node(None)
        self.tail = node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self,item):
        new_node = node(item)
        if self.tail.prev == self.head:
           new_node.next = self.tail
           new_node.prev = self.head
           self.head.next = new_node
           self.tail.prev = new_node
        else:
            temp = self.tail.prev
            new_node.next = self.tail
            new_node.prev = temp
            temp.next = new_node
            self.tail.prev = new_node

    def traverse(self):
        curr = self.head.next
        tail = self.tail

        if curr is tail:
            print("No items to be traversed")

        while curr is not tail:
            print(curr.data)
            curr = curr.next

    def size(self):
        curr = self.head.next
        size = 0
        while curr is not self.tail:
            size += 1
            curr = curr.next
        return size

    def insert(self,pos,item): #assuming linked list is not empty
        new_node = node(item)
        curr = self.head.next
        size =self.size()

        if pos > size:
            print("Position entered is more than the size of the list")
            return

        if pos == 0:
            temp = self.head.next
            new_node.next = temp
            new_node.prev = self.head
            self.head.next = new_node
            temp.prev = new_node
        else:
            while pos > 0 :
                curr = curr.next
                pos -= 1

            temp = curr.prev
            new_node.next = curr
            new_node.prev = temp
            temp.next = new_node
            curr.prev = new_node

    def remove(self, item):
        curr = self.head.next
        found = False

        while curr.next is not self.tail and not found:
            if curr.data == item:
                found = True
            else:
                curr = curr.next
        if found:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = None
            curr.prev = None
            return curr.data











def main():
    d = DoublyLinkedList()

    d.traverse()
    d.append(20)
    d.append(90)
    d.append(50)
    d.append(98)
    d.traverse()
    print("testing insertion")
    d.insert(3,1000)
    d.traverse()

    print("tremoving")
    print("removed "+ str(d.remove(1000)))

    d.traverse()




if __name__ == '__main__':
    main()







