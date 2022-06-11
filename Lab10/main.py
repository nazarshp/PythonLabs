class Node:
    def __init__(self, type, mark, limit, year):
        self.type = type
        self.mark = mark
        self.limit = limit
        self.year = year
        self.nextnode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToEnd(self, type, mark, limit, year):#_aaa
        newbox = Node(type, mark, limit, year)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextnode):
            lastbox = lastbox.nextnode
        lastbox.nextnode = newbox

    def addNode(self, type, mark, limit, year):
        newNode = Node(type, mark, limit, year)
        if (self.head == None):
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode;
            newNode.previous = self.tail;
            self.tail = newNode;
            self.tail.next = None;

    def insert_after_item(self, xyear, type, mark, limit, year):
        n = self.head
        print(n.nextnode)
        while n is not None:
            if n.year == xyear:
                break
            n = n.nextnode
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(type, mark, limit, year)
            new_node.nextnode = n.nextnode
            n.nextnode = new_node

    def sortList(self):
        if (self.head == None):
            return
        else:
            current = self.head
            while (current.nextnode != None):
                index = current.nextnode
                while (index != None):
                    if (current.year > index.year):
                        temp = current.year
                        current.year = index.year
                        index.year = temp
                        temp = current.type
                        current.type = index.type
                        index.type = temp
                        temp = current.mark
                        current.mark = index.mark
                        index.mark = temp
                        temp = current.limit
                        current.limit = index.limit
                        index.limit = temp
                    index = index.nextnode
                current = current.nextnode

    def display(self):
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        while (current != None):
            print(f"{current.type} {current.mark}  {current.limit} {current.year}")
            current = current.nextnode
        print()


if __name__ == "__main__":
    list = LinkedList()
    list.addToEnd("V", "Samsung", 500, 2000)
    list.addToEnd("U", "Samsung", 240, 2001)
    list.addToEnd("A", "Philips", 400, 1998)
    list.addToEnd("V", "LG", 500, 2004)
    list.display()
    list.sortList()
    print("Sorted list: ")
    list.display()
    print("Enter new element: ")
    type_ = input("Enter type: ")
    mark_ = input("Enter mark: ")
    limit_ = int(input("Enter limit: "))
    year_ = int(input("Enter year: "))
    print()
    list.addToEnd(type_, mark_, limit_, year_)
    list.sortList()
    list.display()
