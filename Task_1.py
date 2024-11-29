#Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library. 

#I use home task 13.1
#def count_variables():
    #a = 10
    #b = 20
    #c = a + b
    #d = "Hello, Teacher!"
    #return len(locals())
import unittest
import Some_home_task

class HomeWork13Task1Test(unittest.TestCase):
    def test_count_variables(self):
        variables = Some_home_task.count_variables()
        self.assertEqual(variables, 4)

unittest.main()