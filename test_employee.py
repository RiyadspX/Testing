from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        
    # Setting up the environnement for testing
    def setUp(self):
        print('Setting up')
        self.emp1 = Employee('riyad', 'remili', 50000)
        self.emp2 = Employee('kevin', 'kevi', 60000)
    
    # test and it add some files or do smthing and then u want to delete them after the test 
    def tearDown(self):
        print('TearDown\n')

    def test_email(self):
        print('test emails')
        # This this the env of testing
        #self.emp1 = Employee('riyad', 'remili', 50000)
        #self.emp2 = Employee('kevin', 'kevi', 60000)

        # cheking the emails
        self.assertEqual(self.emp1.email, "riyad.remili@email.com")
        self.assertEqual(self.emp2.email, "kevin.kevi@email.com")

        # Change their values 
        self.emp1.first = 'pierre'
        self.emp2.first = 'hamza'
        # check after changing values
        self.assertEqual(self.emp1.email, "pierre.remili@email.com")
        self.assertEqual(self.emp2.email, "hamza.kevi@email.com")
    
    def test_full_name(self):
        print('test full names')

        self.assertEqual(self.emp1.full_name, "riyad remili")
        self.assertEqual(self.emp2.full_name, "kevin kevi")

        # Change the first name value 
        self.emp1.first = 'pierre'
        self.emp2.first = 'hamza'
        # check after changing values
        self.assertEqual(self.emp1.full_name, "pierre remili")
        self.assertEqual(self.emp2.full_name, "hamza kevi")

    def test_apply_raise(self):
        print('testing the salary raises')
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        #check after the raise
        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

if __name__ == "__main__":
    unittest.main()

        
    
        




