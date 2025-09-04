WITH ranked_salaries AS (
    SELECT e.*,
           DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee e
)
SELECT d.name AS Department,
       r.name AS Employee,
       r.salary AS Salary
FROM ranked_salaries r
JOIN Department d ON r.departmentId = d.id
WHERE r.rnk <= 3;