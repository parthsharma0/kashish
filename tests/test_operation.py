import unittest
from Calculator.operations import add ,sub ,mul ,div

class jenkins(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        
    def test_sub(self):
        self.assertEqual(sub(2,1),1)
        
    def test_mul(self):
        self.assertEqual(mul(2,3),6)
        
    def test_div(self):
        self.assertEqual(div(2,2),1)
        
if __name__ == '__main__':
    unittest.main()