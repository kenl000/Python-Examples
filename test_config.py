import unittest
import yaml

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

class TestStringMethods(unittest.TestCase): 
    # test function to test equality of two value 
    def test_negative(self): 
        firstValue = "geeks"
        secondValue = "gfg"
        # error message in case if test case got failed 
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value 
        day = config.get('Day')
        self.assertEqual(day, "Wednesday", "Error Day")
        self.assertEqual(firstValue, secondValue, message) 

class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]

if __name__ == '__main__':
    unittest.main()
    # unittest.main() will run all tests in the module


#person = Person()
#print('User Abbas has been added with id ', person.set_name('Abbas'))
#print('User associated with id 0 is ', person.get_name(0))

#assertEqual(a,b)           # a==b
#assertNotEqual(a,b) 	    # a != b
#assertTrue(x) 	            # bool(x) is True
#assertFalse(x) 	        # bool(x) is False
#assertIs(a,b) 	            # a is b
#assertIs(a,b) 	            # a is b
#assertIsNot(a, b) 	        # a is not b
#assertIsNone(x) 	x is None
#assertIsNotNone(x) 	x is not None
#assertIn(a, b) 	a in b
#assertNotIn(a, b) 	a not in b
#assertIsInstance(a, b) 	isinstance(a, b)
#assertNotIsInstance(a, b)