SELECT name as Employee
FROM Employee
WHERE salary > (SELECT salary FROM Employee AS Manager WHERE Manager.id = Employee.managerID);
