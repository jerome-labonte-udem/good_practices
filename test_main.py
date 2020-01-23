from unittest import TestCase
from main import my_function


class Test(TestCase):
    def test_my_function(self):
        assert my_function(3, "ha") == "hahaha"
