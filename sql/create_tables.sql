CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50)
);

CREATE TABLE salaries (
    employee_id INT,
    salary DECIMAL(10,2),
    bonus DECIMAL(10,2)
);

CREATE TABLE attendance (
    employee_id INT,
    absence_days INT
);