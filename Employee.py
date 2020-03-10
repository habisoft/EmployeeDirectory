#!/usr/bin/python3

import sys
import argparse
import unittest


'''@package docstring
Documentation for the Employee class

The Employee class is a container for holding an employee's
name, their salary, and their employee ID.

author: Habib Moukalled
email:  habib.moukalled@gmail.com
github: github: https://github.com/HabiSoft
'''

class Employee:
    def __init__(self, ID, name, salary, mgr_ID):
        '''
        Employee constructor/init function

        Parameters:
            ID      (int):  the employee's ID
            name    (str):  the employee's name
            salary  (int):  the employee's salary
            mgr_ID   (int):  the employee's manager ID

        Notes:
            if salary, ID, or mgr_ID are valid integers a value of -1
            will flag that their was an issue, until we have something better
            if mgrID is not a valid integer, None will be used, for example,
            when the employee is the CEO this situation can happen.

        TODO:
            determine if we need a fixed length str for employee's name
        '''
        
        self.ID     = ID if isinstance(ID, int) else -1
        self.name   = name
        self.salary = salary if isinstance(salary, int) else -1
        self.mgr_ID = mgr_ID if isinstance(mgr_ID, int) else None

    def print(self):
        '''
        Print the employee's name

        Parameters:
            none
        '''
        print('- %s\n' % self.name)

class TestEmployee(unittest.TestCase):
    def test_constructor(self):
        employee = Employee(103, 'Jill', 65000, 101)

        self.assertEqual(employee.ID, 103)
        self.assertEqual(employee.name, 'Jill')
        self.assertEqual(employee.salary, 65000)
        self.assertEqual(employee.mgr_ID, 101)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # add optional arguments to the argument parser
    parser.add_argument('-test', '--runtest', action='store_true', help='perform self test on Employee class.')
    parser.add_argument('-doc', '--showdoc', action='store_true', help='print documentation for Employee class.')

    args = parser.parse_args()

    if args.runtest == False and args.showdoc == False:
        parser.print_help()
        sys.exit()

    if args.runtest:
        # Since we are using an argument parser, in order to avoid confusion from the unit test thinking
        # that the arguments are intended for the unit test, we put together a test suite for execution.
        suite = unittest.TestSuite()
        suite.addTest(TestEmployee('test_constructor'))
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif args.showdoc:
        help(Employee)
