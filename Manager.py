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
    def __init__(self, name, salary, ID, mgr_ID, employees):
        '''
        Manager constructor/init function

        Inherited parameters:
            name    (str):  the employee's name
            salary  (int):  the employee's salary
            ID      (int):  the employee's ID
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
        
        Employee.__init__(self, name=name, salary=salary, ID=ID, mgr_ID=mgr_ID)
        self.employees  = employees if isinstance(employees, dict) else dict()

    def add_employee(self, employee):
        employees[employee.name] = employee

    def print(self):
        '''
        Print the employee's name

        Parameters:
            none
        '''
        
        print('\n- %s' % self.name)
        # commented below, since indented is nice for console
        #print('Employees of %s:' % self.name)
        
        for key, value in sorted(self.employees.items()):
            print('\t- %s' % value.name)

class TestManager(unittest.TestCase):
    def test_constructor(self):
        employee1   = Employee('Jill', 65000, 103, 101)
        employee2   = Employee('Bob', 60000, 102, 101)

        employees   = {}
        
        employees[employee1.name] = employee1
        employees[employee2.name] = employee2
        
        mgr_name    = 'Kevin'
        mgr_salary  = 10000000
        mgr_emplID  = 101
        mgr_ID      = 101

        manager = Manager(mgr_name, mgr_salary, mgr_emplID, mgr_ID, employees)

        self.assertEqual(manager.name, mgr_name)
        self.assertEqual(manager.salary, mgr_salary)
        self.assertEqual(manager.ID, mgr_emplID)
        self.assertEqual(manager.mgr_ID, mgr_ID)
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
        # clear out arguments used by the argument parser to keep unittest happy
        # otherwise they will be unrecognized by unittest
        sys.argv[1:] = ''
        unittest.main()
    elif args.showdoc:
        help(Manager)
