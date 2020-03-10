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
    def __init__(self, name, salary, ID, mgr_ID):
        '''
        Employee constructor/init function

        Parameters:
            name    (str):  the employee's name
            salary  (int):  the employee's salary
            ID      (int):  the employee's ID
            mgr_ID   (int):  the employee's manager ID

        Notes:
            if salary, ID, or mgrID are valid integers a value of -1
            will flag that their was an issue, until we have something better
            if mgrID is not a valid integer, None will be used, for example,
            when the employee is the CEO this situation can happen.

        TODO:
            determine if we need a fixed length str for employee's name
        '''
        
        self.name   = name
        self.salary = salary if isinstance(salary, int) else -1
        self.ID     = ID if isinstance(ID, int) else -1
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
        name    = 'Bob'
        salary  = 60000
        ID      = 102
        mgr_ID  = 101

        employee = Employee(name, salary, ID, mgr_ID)

        self.assertEqual(employee.name, name)
        self.assertEqual(employee.salary, salary)
        self.assertEqual(employee.ID, ID)
        self.assertEqual(employee.mgr_ID, mgr_ID)


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
        # clear out arguments used by the argument parser to keep unittest happy
        # otherwise they will be unrecognized by unittest
        sys.argv[1:] = ''
        unittest.main()
    elif args.showdoc:
        help(Employee)
