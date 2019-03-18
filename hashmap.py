from hashmaplinkedlist import HashMapLinkedList


class HashMap(object):
    def __init__(self):
        # Choose a prime number for initial bucket size
        # https://cs.stackexchange.com/a/64191
        self.capacity = 17
        self.size = 0
        self.array = [None] * self.capacity

    def _djb2_hash(self, data):
        # http://www.cse.yorku.ca/~oz/hash.html
        hash = 5381
        for char in data:
            hash += ((hash << 5) + hash) + ord(char)
        return hash

    def _get_index(self, key):
        return self._djb2_hash(key) % self.capacity

    def __getitem__(self, key):
        index = self._get_index(key)
        linked_list = self.array[index]
        if linked_list is None:
            raise KeyError(key)

        result = linked_list.search(key)
        if result is None:
            raise KeyError(key)

        return result


    def __setitem__(self, key, value):
        # uses "separate chaining" to avoid collisions
        # each item in the backing array points to a linked list
        index = self._get_index(key)
        linked_list = self.array[index]

        if linked_list is None:
            linked_list = HashMapLinkedList()
            self.array[index] = linked_list

        linked_list.add_node(key, value)
        self.size += 1

    def __len__(self):
        return self.size

    def remove(self, key):
        index = self._get_index(key)
        linked_list: HashMapLinkedList = self.array[index]
        if linked_list is None:
            raise KeyError(key)
        else:
            value = linked_list.remove_node(key)
            self.size -= 1
            if linked_list.root == None:
                del(linked_list)
                self.array[index] = None

            return value
