#!/usr/bin/python3

import sys
import argparse
import unittest
import csv
import pandas
import numpy

from collections import defaultdict

from Employee import Employee
from Manager import Manager

'''@package docstring
Documentation for a test script


author: Habib Moukalled
email:  habib.moukalled@gmail.com
github: https://github.com/HabiSoft
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
            # but this is what we are using for now
            empl_id_idx = 0
            name_idx    = 1
            salary_idx  = 2
            mgr_id_idx  = 3

            mgr_IDs     = set()
            employees   = {}
            managers    = {}
            manager_map = defaultdict(list)
            reports     = {}
            
            # skip over the CSV-file's header
            next(csv_reader)
            
            ceo_manager = {}

            # now iterate through the rest of the CSV file
            for row in csv_reader:
                ID      = int(row[empl_id_idx])
                name    = str(row[name_idx])
                salary  = int(row[salary_idx])
                
                try:
                    mgr_ID = int(row[mgr_id_idx])
                except ValueError:
                    # if we get an exception that means we are trying to convert None to an int()
                    mgr_ID = -1
                    ceo_manager = Manager(ID, name, salary, mgr_ID, None)

                print('ID: %d, name: %s, salary: %d, mgr_ID: %d' % (ID, name, salary, mgr_ID))

                # build a list of manager IDs without duiplicates
                mgr_IDs.add(mgr_ID)
                employee        = Employee(ID, name, salary, mgr_ID)
                employees[ID]   = employee
                
                if employee.mgr_ID == ceo_manager.ID:
                    ceo_manager.add_employee(employee)
                
            # let's handle the CEO first, as it is our base case:
            #ceo_manager.print()
            managers[ceo_manager.ID] = ceo_manager

            for mgr_ID in mgr_IDs:
                if employee.mgr_ID == -1:
                    managers[mgr_ID] = ceo_manager
                else:
                    managers[mgr_ID] = Manager(mgr_ID, None, None, None, -1)

            for ID, employee in employees.items():
                if employee.mgr_ID != -1:
                    mgr             = employees[employee.mgr_ID]
                    manager         = managers[employee.mgr_ID]
                    manager.ID      = mgr.ID
                    manager.name    = mgr.name
                    manager.salary  = mgr.salary
                    manager.mgr_ID  = employees[manager.ID].mgr_ID
                    
                    manager.add_employee(employee)
                    managers[manager.ID] = manager
            
            for mgr_ID, manager in managers.items():
                manager.print()

            #ceo_manager.print()

        '''
            managers = {}
            managers[ceo_manager.ID] = ceo_manager

            for ID, employee in employees.items():

            for mgr_ID in sorted(mgr_IDs):
                # if our mgr_ID is -1, skip it, as we already handled it
                if mgr_ID == -1:
                    continue
                
                ID      = employees[mgr_ID].ID
                name    = employees[mgr_ID].name
                salary  = employees[mgr_ID].salary
                mgr_ID  = employees[mgr_ID].mgr_ID
                

                managers[ID].add_employee(
                #manager = Manager
            '''
'''
        # use pandas to ingest the CSV file, here we provde the expected column header format
        data_frame = pandas.read_csv('Employees.csv', names=['ID', 'Employee Name', 'Salary', 'Manager ID'])
        print(data_frame)

        # build a relation between employee ID and the ID of the manager they report to
        empl_mgr_map = dict(zip(data_frame['ID'].values[1:], data_frame['Manager ID'].values[1:]))
        print(empl_mgr_map)
        
        # find the entry in the data where the manager ID is None/NULL, this corresponds to our CEO
        # for this implementation we are assuming that there will only be one entry with a None/NULL
        # for the manager ID this assumption is likely dangerous for production code
        ceo_data    = data_frame[data_frame['Manager ID'].isnull()]
        ceo_ID      = int(ceo_data['ID'].values[0])
        ceo_name    = ceo_data['Employee Name'].values[0]
        ceo_salary  = int(ceo_data['Salary'].values[0])
        ceo_mgr_ID  = None
        
        ceo_manager = Manager(ceo_ID, ceo_name, ceo_salary, ceo_mgr_ID, None)
        
        # the first element is the column header, so let's skip it
        mgr_IDs = data_frame['Manager ID'].values[1:]

        managers = {}
        for mgr_ID in mgr_IDs:
            if mgr_ID == ceo_manager.mgr_ID:
                print('found NaN')
                continue

            manager_data = data_frame[data_frame['ID'] == mgr_ID]
            #manager = Manager(
            #print(manager_data.values)
            print(mgr_ID)
            #managers[mgr_ID] 

        #for index, row in data_frame.iterrows():
        #    print(row)
        #print(manager_groups)
        #for key, value in sorted((value, key) for (key, value) in empl_mgr_map.items()):
        #    print('empl_ID: %s, mgr_ID: %s' % (empl_ID, mgr_ID))
        
        #for empl_ID, mgr_ID in sorted(empl_mgr_map.items()):
        #    print('empl_ID: %s, mgr_ID: %s' % (empl_ID, mgr_ID))

        #manager_data = data_frame[data_frame['Manager ID'] == ceo_ID]
        #manager_data = data_frame.groupby(['Manager ID']).groups
        #print(manager_data)

        #for item in manager_data.itertuples():
        #    print(item)

        #while manager_data != None:
        #    print(manager_data)
            
        #ceo_manager.print()
'''

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
