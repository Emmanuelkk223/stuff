
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    salary DECIMAL(10, 2),
    department_id INT
);

CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(255)
);

-- Insert data into Employees table
INSERT INTO Employees (emp_id, first_name, last_name, salary, department_id) VALUES
    (1, 'John', 'Doe', 60000.00, 1),
    (2, 'Jane', 'Smith', 70000.00, 2),
    (3, 'Peter', 'Jones', 55000.00, 1),
    (4, 'Mary', 'Brown', 80000.00, 2),
    (5, 'David', 'Wilson', 65000.00, 1);

-- Insert data into Departments table
INSERT INTO Departments (dept_id, dept_name) VALUES
    (1, 'Sales'),
    (2, 'Marketing');

-- Retrieve employee information with their department names
SELECT 
    e.first_name,
    e.last_name,
    e.salary,
    d.dept_name
FROM 
    Employees e
JOIN 
    Departments d ON e.department_id = d.dept_id;
[/mid]


