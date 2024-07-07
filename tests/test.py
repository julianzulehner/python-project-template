import unittest
from mypackage.mymodule import myfunc

class TestMypackage(unittest.TestCase):

    def test_myfunc(self):
        teststring = "Hello from my package"
        self.assertEqual(teststring, myfunc())

if __name__ == '__main__':
    unittest.main()