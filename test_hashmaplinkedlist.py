import pytest

from hashmaplinkedlist import HashMapLinkedList


class TestHashMapLinkedList(object):
    def test_init(self):
        linked_list = HashMapLinkedList()
        assert linked_list.root == None

    def test_append(self):
        linked_list = HashMapLinkedList()
        linked_list.add_node(1, "abc")
        assert linked_list.root.key == 1
        assert linked_list.root.value == "abc"
        assert linked_list.root.next == None

    def test_append_multiple(self):
        linked_list = HashMapLinkedList()
        linked_list.add_node(1, "abc")
        linked_list.add_node(2, "def")
        linked_list.add_node(3, "ghi")
        linked_list.add_node(4, "jkl")

        all_nodes = linked_list.all_nodes()

        assert all_nodes[0].key == 1
        assert all_nodes[0].value == "abc"

        assert all_nodes[1].key == 2
        assert all_nodes[1].value == "def"

        assert all_nodes[2].key == 3
        assert all_nodes[2].value == "ghi"

        assert all_nodes[3].key == 4
        assert all_nodes[3].value == "jkl"

    def test_search(self):
        linked_list = HashMapLinkedList()
        linked_list.add_node(1, "abc")
        linked_list.add_node(2, "def")
        linked_list.add_node(3, "ghi")
        linked_list.add_node(4, "jkl")

        result = linked_list.search(1)
        assert result == "abc"

        result = linked_list.search(2)
        assert result == "def"

        result = linked_list.search(3)
        assert result == "ghi"

        result = linked_list.search(4)
        assert result == "jkl"

    def test_remove_root(self):
        linked_list = HashMapLinkedList()
        linked_list.add_node(1, "abc")
        linked_list.add_node(2, "def")

        linked_list.remove_node(1)

        assert linked_list.root.key == 2
        assert linked_list.root.value == "def"
        assert linked_list.root.next == None

    def test_remove_middle(self):
        linked_list = HashMapLinkedList()
        linked_list.add_node(1, "abc")
        linked_list.add_node(2, "def")
        linked_list.add_node(3, "ghi")
        linked_list.add_node(4, "jkl")

        linked_list.remove_node(2)

        nodes = linked_list.all_nodes()
        assert len(nodes) == 3

        assert nodes[0].key == 1
        assert nodes[1].key == 3
        assert nodes[2].key == 4

    def test_remove_end(self):
        linked_list = HashMapLinkedList()
        linked_list.add_node(1, "abc")
        linked_list.add_node(2, "def")
        linked_list.add_node(3, "ghi")
        linked_list.add_node(4, "jkl")

        linked_list.remove_node(4)

        nodes = linked_list.all_nodes()
        assert len(nodes) == 3

        assert nodes[0].key == 1
        assert nodes[1].key == 2
        assert nodes[2].key == 3

    def test_remove_keyerror(self):
        linked_list = HashMapLinkedList()
        linked_list.add_node(1, "abc")
        linked_list.add_node(2, "def")

        with pytest.raises(KeyError):
            linked_list.remove_node(3)
