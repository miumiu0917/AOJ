def main():
    n = int(input())
    lst = DoublyLinkedList()

    for _ in range(n):
        inputs = input().split(' ')
        command = inputs[0]
        if command == 'insert':
            lst.insert(int(inputs[1]))
        elif command == 'delete':
            lst.delete(int(inputs[1]))
        elif command == 'deleteFirst':
            lst.popleft()
        elif command == 'deleteLast':
            lst.pop()
    print(lst)


class DoublyLinkedList:

    def __init__(self):
        self.node = None
    
    def insert(self, value):
        node = Node(value)
        if self.node is None:
            self.node = node
        else:
            self.node.prev = node
            node.next = self.node
            self.node = node
    
    def popleft(self):
        node = self.node
        self.node = self.node.next
        if self.node is None:
            return
        self.node.prev = None
        return node
    
    def pop(self):
        if self.node is None:
            return
        node = self.node
        while node.next is not None:
            node = node.next
        if node.prev is None:
            self.node = None
            return
        node.prev.next = None
        return node
    
    def delete(self, value):
        if self.node is None:
            return
        node = self.node
        while node is not None and node.value != value:
            node = node.next
        if node is None:
            return
        if node.next is None:
            self.pop()
            return
        if node.prev is None:
            self.popleft()
            return
        node.prev.next, node.next.prev = node.next, node.prev

    def __repr__(self):
        s = ''
        node = self.node
        while node is not None:
            s += str(node.value) + ' '
            node = node.next
        return s.strip()


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


if __name__ == '__main__':
    main()