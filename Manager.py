#!/usr/bin/python3

import sys
import argparse
import unittest

from Employee import Employee

'''@package docstring
Documentation for the Manager class

The Manager class is a class that is derived from
the Employee class that inherits the member variables
name, salary, and ID. It implements the manager ID

author: Habib Moukalled
email:  habib.moukalled@gmail.com
github: https://github.com/HabiSoft
'''

class Manager(Employee):
    def __init__(self, ID, name, salary, mgr_ID, employees):
        '''
        Manager constructor/init function

        Inherited parameters:
            ID      (int):  the employee's ID
            name    (str):  the employee's name
            salary  (int):  the employee's salary
            mgr_ID  (int):  the manager's ID
        
        Parameters of the derived Manager class:
            employees (dict): the employees that report to the manager

        Notes:
            if either salary, ID  are not valid integers, a value of -1
            will flag that their was an issue. If mgrID is not a valid integer
            the value of None will be used, for example the CEO will not have a manager.

        TODO:
            determine if we need a fixed length str for employee's name
        '''
        
        Employee.__init__(self, ID=ID, name=name, salary=salary, mgr_ID=mgr_ID)
        self.employees  = employees if isinstance(employees, dict) else dict()

    def add_employee(self, employee):
        self.employees[employee.name] = employee

    def print(self):
        '''
        Print the employee's name

        Parameters:
            none
        '''
        
        print('\n- %s' % self.name)
        # commented below, since indented is nice for console
        #print('Employees of %s:' % self.name)
        
        for ID, employee in sorted(self.employees.items()):
            print('\t- %s' % employee.name)

class TestManager(unittest.TestCase):
    def test_constructor(self):
        employees               = {}
        employee                = Employee(104, 'Zane', 85000, 101)
        employees[employee.ID]  = employee
        
        manager = Manager(101, 1000000, 'Kevin', None, employees)

        self.assertEqual(manager.ID, 101)
        self.assertEqual(manager.name, 'Kevin')
        self.assertEqual(manager.salary, 1000000)
        self.assertEqual(manager.mgr_ID, None)
        self.assertEqual(manager.employees, employees)

        manager.print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # add optional arguments to the argument parser
    parser.add_argument('-test', '--runtest', action='store_true', help='perform self test on Manager class.')
    parser.add_argument('-doc', '--showdoc', action='store_true', help='print documentation for Employee class.')

    args = parser.parse_args()

    if args.runtest == False and args.showdoc == False:
        parser.print_help()
        sys.exit()

    if args.runtest:
        # Since we are using an argument parser, in order to avoid confusion from the unit test thinking
        # that the arguments are intended for the unit test, we put together a test suite for execution.
        suite = unittest.TestSuite()
        suite.addTest(TestManager('test_constructor'))
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif args.showdoc:
        help(Manager)
