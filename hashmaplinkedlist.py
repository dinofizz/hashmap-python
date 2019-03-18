from hashmapnode import HashMapNode


class HashMapLinkedList(object):
    def __init__(self):
        self.root = None

    def search(self, key):

        if self.root is None:
            return None

        if self.root.key == key:
            return self.root.value

        temp_node = self.root.next

        while temp_node is not None:
            if temp_node.key == key:
                return temp_node.value
            temp_node = temp_node.next

        return None

    def add_node(self, key, value):
        new_node = HashMapNode(key, value)

        if self.root is None:
            self.root = new_node
            return

        if self.root.key == key:
            self.root.value = value
            return

        if self.root.next is None:
            self.root.next = new_node
            return

        temp = self.root.next

        while temp is not None:
            if temp.key == key:
                temp.value = value
                return
            if temp.next is None:
                temp.next = new_node
                return
            temp = temp.next

    def remove_node(self, key):
        if self.root is None:
            raise KeyError(key)

        if self.root.key == key:
            temp = self.root
            self.root = temp.next
            temp_value = temp.value
            del(temp)
            return temp_value

        previous = self.root
        current = self.root.next

        while current is not None:
            if current.key == key:
                previous.next = current.next
                temp_value = current.value
                del(current)
                return temp_value
            previous = current
            current = current.next

        raise KeyError(key)

    def all_nodes(self):
        all_nodes = []
        temp = self.root
        while temp is not None:
            all_nodes.append(temp)
            temp = temp.next
        return all_nodes
