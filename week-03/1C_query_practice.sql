USE northwind;
-- Write a query to list the product id, product name, and unit price of every product. This time, display them in ascending order by price.
select ProductID, ProductName, UnitPrice
from products
order by UnitPrice ASC; 

-- What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price.
select ProductID, ProductName, UnitPrice, UnitsInStock
from products
Where UnitsInStock >= 100
order by UnitPrice DESC;

-- What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price. If two or more have the same price, list those in ascending order by product name.
select ProductID, ProductName, UnitPrice, UnitsInStock
from products
Where UnitsInStock >= 100
order by Unitprice DESC,
productName ASC;

-- Write a query against the orders table that displays the total number of distinct customers who have placed orders
-- based on customer ID. Use an alias to label the count calculation as CustomerCount.

SELECT ShipCountry,
       COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders
WHERE ShipCountry IS NOT NULL
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- What are the products that we carry where we have less than 25 units on hand, but 1 or more units of them are on order? Write a query that orders them by quantity on order (high to low), then by product name.
SELECT ProductName, UnitsInStock, UnitsOnOrder
from products
Where UnitsInStock<=25
And UnitsonOrder>1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- rite a query to list each of the job titles in employees, along with a count of how many employees hold each job title.

SELECT Title,
       COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title
ORDER BY EmployeeCount DESC;

-- What employees have a monthly salary that is between $2000 and $2500? Write a query that orders them by job title.
SELECT Title,
       FirstName,
       LastName,
       Salary
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title ASC;
