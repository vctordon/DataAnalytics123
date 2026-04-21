USE northwind;
-- comment practice using ctrl /

-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells. (Hint: To help set up your query, look at the schema preview to see what column names belong to each table. Or use SELECT * to query all columns first, then refine your query to just the columns you want.)
SELECT ProductID, productName, UnitPrice FROM products;

-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT*
From products 
WHERE UnitPrice <= 7.50; 

-- What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question
SELECT*
From Products
Where UnitsInStock = 0; 

-- Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry. CategoryID
-- can be identified by using the category ID - The list can be found under categories table 

SELECT CategoryID, CategoryName,Description
From Categories; 

-- Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers? Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.
-- To find the supplier info (Tokyo Traders is ID 4) 
SELECT SupplierID, CompanyName, ContactName, ContactTitle, Address
From Suppliers;

-- Products from supplier 
SELECT ProductName, SupplierID
FROM Products
WHERE SupplierID = 4;

-- How many employees work at northwind? What employees have "manager" somewhere in their job title? Write queries to answer each question.
SELECT count(*) as Employees
from employees; 
-- Total number = 9 employees 

select EmployeeID, FirstName, LastName, Title
from employees
where title LIKE '%manager%'; 

-- Employee Steven B Sales Manager 

