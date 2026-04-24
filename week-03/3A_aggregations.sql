USE northwind; 

-- Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price. 

SELECT
MIN(UnitPrice) AS CheapestItem
FROM products;

-- Second Query 

SELECT
    ProductName,
    UnitPrice
FROM products
WHERE UnitPrice = (
    SELECT MIN(UnitPrice)
    FROM products
);


-- Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.)

SELECT 
round(avg(UnitPrice), 0) AS "Average Price"
 FROM products;
 
 -- BONUS: 
 SELECT 
round(avg(UnitPrice), 2)
AS "Average Price"
FROM products;

-- Write a query to find the price of the most expensive item that Northwind sells. Then
-- Write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

SELECT 
MAX(UnitPrice) AS "Most Expensive" 
FROM products;


SELECT
    P.ProductName,
    P.UnitPrice,
    S.CompanyName AS "Supplier Name"
FROM products AS P
JOIN suppliers AS S
    ON P.SupplierID = S.SupplierID
WHERE P.UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM products
);

-- Write a query to find total monthly payroll (the sum of all the employees’ monthly  
-- salaries)

SELECT
	SUM(Salary) AS "Total Monthly Payroll" 
FROM Employees; 

SELECT
round(SUM(Salary),2) AS "Total Monthly Payroll" 
FROM Employees; 

-- Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)

SELECT 
	MAX(Salary) AS "Highest Paid",
    MIN(Salary) AS "Lowest Paid" 
FROM Employees; 


-- Write a query to find the name and supplier ID of each supplier and the number of
-- items they supply. Hint: Join is your friend here.

SELECT 
S.SupplierID,
S.CompanyName,
COUNT(P.ProductID) AS "Number of Items" 
FROM Suppliers AS S
JOIN Products AS P 
ON P.SupplierID = S.SupplierID
GROUP BY S.supplierID; 

-- Write a query to find the list of all category names and the average price for items in
-- each category

SELECT
C.CategoryName, 
P.ProductName,
AVG(UnitPrice) AS "Average Price from Items" 
FROM categories AS C
JOIN products AS P
ON C.CategoryID = P.CategoryID
GROUP BY C.CategoryName, 
P.ProductName; 

-- Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply.

SELECT 
S.CompanyName,
S.SupplierID,
COUNT(P.ProductID) AS "Number of Items" 
FROM Suppliers AS S
JOIN Products AS P 
ON P.SupplierID = S.SupplierID
GROUP BY S.SupplierID,
S.CompanyName
HAVING COUNT(P.ProductID)>=5; 

-- Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list 

SELECT
ProductName,
ProductID,
UnitsInStock * UnitPrice AS "Inventory Value"
FROM products
WHERE UnitsinStock >0 
ORDER BY  
ProductName ASC; 

