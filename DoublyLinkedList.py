class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        prev_node = node
        next_node = node.next
        new_node = DoublyLinkedList.Node(val, next_node, prev_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self]) + "]"




    # implement get method worst-time O(i)
    def __getitem__(self, i):
        """return the value at ith node. If i is out of range, and IndexError is raised """
        if i >= len(self) or i < 0:
            raise Exception("Index is out of error")
        if i < len(self)//2:
            node = self.header
            for k in range(i + 1):
                node = node.next
            return node.data
        else:
            node = self.trailer
            for k in range(len(self) - i):
                node = node.prev
            return node.data

    def move_to_end(self, node):
        if node is self.trailer.prev:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.trailer.prev
            node.next = self.trailer
            self.trailer.prev.next = node
            self.trailer.prev = node

