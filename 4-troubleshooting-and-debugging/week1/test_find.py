from unittest import TestCase

from find import find_item

class TestFind(TestCase):
    def benchmark(self):
        list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]
        res = find_item(list_of_names, "Alex")  # True)
        self.assertEqual(res, True)