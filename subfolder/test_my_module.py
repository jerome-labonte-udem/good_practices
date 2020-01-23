from unittest import TestCase
from .my_module import another_function

class Test(TestCase):
    def test_another_function(self):
        assert another_function(2, 3)==5
