# EmployeeDirectory
Author: Habib Moukalled
Email:  habib.moukalled@gmail.com
url:    https://github.com/habisoft/EmployeeDirectory

Implement a directory of employees given their name, salary, ID, and reporting manager ID. Implemented in Python 3

The Employee class is an object for storing an employee's
name, salary, employee ID, and their reporting manager ID.

The Manager class is a derived class from the Employee class
that inherits all the properties of the base class but adds
a member variable for storing a collection of employees.

Both of the classes above are implemented using Python 3. The
scripts can be run indepently, and in this case wold trigger
a self test. Ensure the scripts are made executable:

chmod a+x Employee.py
chmod a+x Manager.py


The scripts are tested under CentOS 7, therefore, the Python 3
path specified at the top of the sript might have to be edited
to accomodate the environment.

The script that will run the full program is the TestEmployeeHierarchy.py,
again, make it an executable:

chmod a+x TestEmployeeHierarchy.py

Then to run the full set of tests:

./TestEmployeeHierarchy.py -test

And it will print out successes and failures.

The input data is provided by Employees.csv. At the moment,
the scripts expect it to be in the directory where the scripts
are. There is no exception handling around the file being missing, obviously
for a production system this would not be acceptable

The indentation of the hierarchy is not working at the moment. Given more time,
a better approach than the one I cobbled together would be to use a directed 
graph with edges to represent the relationship between employees and managers.

My solution takes O(3N), since I take three passes through the data:
Pass 1: loading the data, accumulate the manager IDs, and accumulate salary.
Pass 2: create the manager instances from the data in Pass 1.
Pass 3: fill in the manager employee hierarchy.

I believe there is a dynamic programming approach when a directed graph is used
that achieves the above in O(N).

Another viable solution would be to use a library like Pandas to load the CSV-file data
which allows you to slice the data in many ways and in some cases use it to query the data directly.
For example aggreate data like salary is a one liner once it's in a Pandas data frame.

Some additonal boundary cases that are interesting to test:
1.) Several levels of nested hierarchy
2.) What happens when garbage data is provided in the CSV-file
3.) More testing around re-using the same ID and manager ID.
