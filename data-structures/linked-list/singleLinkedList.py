class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        return

    def search_item(self, value):
        current_node = self.head
        current_id = 1
        while current_node is not None:
            if current_node.data == value:
                return current_id
            else:
                current_node = current_node.next
                current_id = current_id + 1

    def remove_item(self, item_id):
        current_node = self.head
        prev_node = None
        current_id = 1
        while current_node is not None:
            if current_id == item_id:
                if prev_node is not None:
                    prev_node.next = current_node.next
                    return
                else:
                    self.head = current_node.next
                    return
            else:
                prev_node = current_node
                current_node = current_node.next
                current_id = current_id + 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def list_length(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count


node1 = ListNode(10)
node2 = ListNode(8.2)
item3 = "Xinhe"
node4 = ListNode(200)
node5 = True

mylist = SingleLinkedList()
for i in [node1, node2, item3, node4, node5]:
    mylist.add_item(i)

mylist.print_list()
print('length = ', mylist.list_length())
print('"Xinhe" is in node:', mylist.search_item('Xinhe'))

print('-----------------')

mylist.remove_item(3)
mylist.remove_item(1)
mylist.print_list()
