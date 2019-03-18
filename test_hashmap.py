import pytest

from hashmap import HashMap


class TestHashMap(object):
    def test_init(self):
        hash_map = HashMap()
        assert hash_map.capacity == 17
        assert len(hash_map.array) == 17
        assert len(hash_map) == 0

        for item in hash_map.array:
            assert item is None

    def test_add_item(self):
        hash_map = HashMap()
        hash_map["abc"] = "def"
        assert hash_map["abc"] == "def"

    def test_add_collision(self):
        key1 = "hysh"
        key2 = "vwtuyy"

        hash_map = HashMap()
        hash_map[key1] = True
        hash_map[key2] = False

        assert len(hash_map) == 2

        assert hash_map[key1] == True
        assert hash_map[key2] == False

    def test_keyerror_empty(self):
        with pytest.raises(KeyError):
            hash_map = HashMap()
            print(hash_map["foo"])

    def test_keyerror(self):
        with pytest.raises(KeyError):
            hash_map = HashMap()
            hash_map["moo"] = True
            print(hash_map["foo"])

    def test_remove(self):
        hash_map = HashMap()
        hash_map["moo"] = True

        assert hash_map.remove("moo") == True
        assert len(hash_map) == 0

    def test_remove_keyerror(self):
        hash_map = HashMap()
        hash_map["moo"] = True

        with pytest.raises(KeyError):
            hash_map.remove("foo")

    def test_combo_add_remove(self):
        hash_map = HashMap()
        hash_map["abc"] = True
        hash_map["moo"] = False
        hash_map["goo"] = True
        hash_map["foo"] = False

        assert len(hash_map) == 4

        hash_map.remove("goo")
        hash_map.remove("abc")

        assert len(hash_map) == 2

        hash_map["goo"] = False

        assert len(hash_map) == 3

    def test_multi_write_and_read(self):
        python_dict = {}
        with open("test_data.csv", "r") as file:
            for line in file:
                split = line.split(",")
                python_dict[split[0].strip()] = split[1].strip()

        hash_map = HashMap()

        for original_key in python_dict:
            hash_map[original_key] = python_dict[original_key]

        assert len(hash_map) == 100

        for original_key in python_dict:
            assert hash_map[original_key] == python_dict[original_key]
