""" To run this file make python -m unittest test_calc.py
or by name in main and then just by python test_calc.py
tests dont run in ordr of script
"""
# This part is because i'm having an error : ModuleNotFoundError: No module named 'src.calc'
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Solution 2 is to run the command python -m tests.test_calc



from src.calc import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    """ This a test for the calculator class
    """
    def test_add(self):  # Should start with the test_functionNAME
        # The assert is not a test the function is 1 test even with 100 of asserts
        # Adding more asserts make a test good
        # We dont have to add a lot of tests 
    
        self.assertEqual(Calculator(10, 15).add(), 25)
        self.assertEqual(Calculator(-1, 1).add(), 0)  # The test will fail it's considered as one test for these two
        self.assertEqual(Calculator(-1, 0).add(), -1)
    
    def test_substract(self):  
    
        self.assertEqual(Calculator(10, 15).substract(), -5)
        self.assertEqual(Calculator(-1, 1).substract(), -2)  
        self.assertEqual(Calculator(-1, 0).substract(), -1)
    
    def test_multiply(self):  
    
        self.assertEqual(Calculator(10, 15).multiply(), 150)
        self.assertEqual(Calculator(-1, 1).multiply(), -1)  
        self.assertEqual(Calculator(-1, 0).multiply(), 0)
    
    def test_divide(self):  
    
        self.assertEqual(Calculator(10, 10).divide(), 1)
        self.assertEqual(Calculator(-1, 1).divide(), -1)  
        self.assertEqual(Calculator(22, 2).divide(), 11)
        
        # Test the raises
        #self.assertRaises(ValueError, Calculator(-1, 0).divide())
        # This executes the method before assertRaises has a chance to check for the exception

        # Solution 1 : for any divide function 
        # To fix this, you should pass the callable (the divide method) to assertRaises without actually calling it. 
        # You can do this using a lambda or by specifying the arguments separately.
        self.assertRaises(ValueError, lambda: Calculator(-1, 0).divide())

        # Solution 2 : Since divide doesnt take any arguments 
        # Pass it without parentheses
        self.assertRaises(ValueError, Calculator(-1, 0).divide)

        # Test the raises with context manager
        with self.assertRaises(ValueError):
            Calculator(-1, 0).divide()

        
if __name__ == '__main__':
    
    unittest.main()
    

        