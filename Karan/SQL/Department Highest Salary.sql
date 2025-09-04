SELECT Department.name AS Department,
       Employee.name AS Employee,
       Employee.salary AS Salary
FROM (
    SELECT *,
           RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
) Employee
JOIN Department ON Employee.departmentId = Department.id
WHERE rnk = 1;