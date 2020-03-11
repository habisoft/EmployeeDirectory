#!/usr/bin/python3

import sys
import argparse
import unittest
import csv

from Employee import Employee
from Manager import Manager

'''@package docstring
Documentation for a test script


author: Habib Moukalled
email:  habib.moukalled@gmail.com
github: https://github.com/habisoft/EmployeeDirectory
'''

class TestEmployeeHierarchy(unittest.TestCase):
    # test the Employee's constructor/init
    def test_employee_constructor(self):
        employee = Employee(103, 'Jill', 65000, 101)

        self.assertEqual(employee.ID, 103)
        self.assertEqual(employee.name, 'Jill')
        self.assertEqual(employee.salary, 65000)
        self.assertEqual(employee.mgr_ID, 101)

    # test the Manager's constructor/init
    def test_manager_constructor(self):
        employee1   = Employee(104, 'Zane', 85000, 101)
        employee2   = Employee(103, 'Jill', 65000, 101)
        employee3   = Employee(102, 'Bob', 60000, 101)
        
        employees   = {}
        
        employees[employee2.ID] = employee1
        employees[employee1.ID] = employee2
        employees[employee2.ID] = employee3
        
        manager = Manager(101, 'Kevin', 1000000, None, employees)

        self.assertEqual(manager.ID, 101)
        self.assertEqual(manager.name, 'Kevin')
        self.assertEqual(manager.salary, 1000000)
        self.assertEqual(manager.mgr_ID, None)
        self.assertEqual(manager.employees, employees)

    # use a CSV file to see a test for the entire employee hierarchy
    def test_employee_hierarchy(self):
        with open('Employees.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # there is likely a more elegant way to index into the CSV file
            # but this is what we are using for now, for exmaple, if we 
            # use something like pandas we can query the data much like a database
            empl_id_idx     = 0
            name_idx        = 1
            salary_idx      = 2
            mgr_id_idx      = 3

            mgr_IDs         = set()
            ceo_ID          = -1
            employees       = {}
            total_salary    = 0

            # skip over the CSV-file's header
            next(csv_reader)
                        
            #employees[0] = Employee(-1, None, None, None)

            # now iterate through the rest of the CSV file
            for row in csv_reader:
                ID              = int(row[empl_id_idx])
                name            = str(row[name_idx])
                salary          = int(row[salary_idx])
                total_salary    = total_salary + salary # accumulate our total salary

                try:
                    mgr_ID = int(row[mgr_id_idx])
                except ValueError:
                    # if we get an exception that means we are trying to convert None to an int()
                    # this means we are looking at the CEO's manager ID.
                    mgr_ID = 0
                    ceo_ID  = ID

                print('ID: %d, name: %s, salary: %d, mgr_ID: %d' % (ID, name, salary, mgr_ID))

                # build a list of manager IDs without duiplicates
                mgr_IDs.add(mgr_ID)
                employee        = Employee(ID, name, salary, mgr_ID)
                employees[ID]   = employee
                
            # Build and initialize a list of managers using the
            # manager IDs we collected above
            managers = {}
            for mgr_ID in mgr_IDs:
                if mgr_ID != 0:
                    employee = employees[mgr_ID]
                    managers[mgr_ID] = Manager(employee.ID, employee.name, employee.salary, employee.mgr_ID, None)

            # one final pass to build up the manager/employee hierarchy
            for ID, employee in employees.items():
                if employee.ID not in mgr_IDs:
                    managers[employee.mgr_ID].add_employee(employee)
                elif employee.mgr_ID != 0:
                    managers[employee.mgr_ID].add_employee(managers[employee.ID])

            # print our organization hierarchy
            managers[ceo_ID].print()

            # build a formatted salary string and print it
            salary_string = format(total_salary, ',d')
            print('\nTotal salary: $%s' % salary_string)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # add optional arguments to the argument parser
    parser.add_argument('-test', '--runtest', action='store_true', help='perform the suite of unit tests.')
    parser.add_argument('-doc', '--showdoc', action='store_true', help='print documentation for Employee class.')

    args = parser.parse_args()

    if args.runtest == False and args.showdoc == False:
        parser.print_help()
        sys.exit()

    if args.runtest:
        # Since we are using an argument parser, in order to avoid confusion from the unit test thinking
        # that the arguments are intended for the unit test, we put together a test suite for execution.
        suite = unittest.TestSuite()
        
        suite.addTest(TestEmployeeHierarchy('test_employee_constructor'))
        suite.addTest(TestEmployeeHierarchy('test_manager_constructor'))
        suite.addTest(TestEmployeeHierarchy('test_employee_hierarchy'))

        unittest.TextTestRunner(verbosity=2).run(suite)

    elif args.showdoc:
        help(Employee)
        help(Manager)
