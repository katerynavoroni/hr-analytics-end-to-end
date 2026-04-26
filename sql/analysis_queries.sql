-- Average salary by department
SELECT 
    department,
    AVG(salary) AS avg_salary
FROM employees e
JOIN salaries s
    ON e.employee_id = s.employee_id
GROUP BY department
ORDER BY avg_salary DESC;

-- Total bonus by department
SELECT 
    department,
    SUM(bonus) AS total_bonus
FROM employees e
JOIN salaries s
    ON e.employee_id = s.employee_id
GROUP BY department
ORDER BY total_bonus DESC;

-- Average absence
SELECT 
    department,
    AVG(absence_days) AS avg_absence
FROM employees e
JOIN attendance a
    ON e.employee_id = a.employee_id
GROUP BY department
ORDER BY avg_absence DESC;

--top_employees
SELECT 
    e.employee_id,
    e.department,
    s.salary,
    s.bonus,
    (s.salary + s.bonus) AS total_compensation
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id
ORDER BY total_compensation DESC
LIMIT 5;

--kpi
SELECT 
    e.employee_id,
    e.department,
    s.salary,
    a.absence_days,
    ROUND(a.absence_days / 2.0, 2) AS avg_absence_per_month
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id
JOIN attendance a ON e.employee_id = a.employee_id;

--korelacja
SELECT 
    e.employee_id,
    e.department,
    s.salary,
    a.absence_days
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id
JOIN attendance a ON e.employee_id = a.employee_id
ORDER BY s.salary DESC;

--payroll_summary
SELECT 
    SUM(s.salary) AS total_salary_cost,
    SUM(s.bonus) AS total_bonus_cost,
    SUM(s.salary + s.bonus) AS total_compensation_cost,
    COUNT(e.employee_id) AS total_employees
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id;


--dbeaver_query_result_example
SELECT 
    e.employee_id,
    e.department,
    s.month,
    s.salary,
    s.bonus,
    a.hours_worked,
    a.absence_days
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id
JOIN attendance a 
    ON e.employee_id = a.employee_id 
   AND s.month = a.month;