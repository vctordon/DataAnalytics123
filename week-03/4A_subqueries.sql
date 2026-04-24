-- What is the product name(s) of the most expensive products?
-- HINT: Find the max price in a subquery and then use that value to find products
-- whose price equals that value. (Some of your answers from Exercise 3.A may offer a
-- useful starting point.).

SELECT 
ProductName, UnitPrice,
(SELECT MAX(UnitPrice) FROM Products) AS "Most Expensive" 
FROM products
ORDER BY UnitPrice desc; 

-- What is the product name(s) and categories of the least expensive products?
-- HINT: Find the min price in a subquery and then use that in your more complex
-- query that joins products with categories

-- SUBQUERY SELECT
-- MIN(UnitPrice) AS CheapestItem
-- FROM products;

SELECT
P.ProductName,
P.UnitPrice AS "Cheapest Price",
C.CategoryID
FROM Products AS P
JOIN categories AS C 
ON C.CategoryID = P.CategoryID 
WHERE P.UnitPrice = (SELECT MIN(UnitPrice) AS CheapestItem FROM products);

-- What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?
-- HINT: Find the shipper id of "Federal Shipping" in a subquery and then use that
-- value to find the orders that used that shipper.
-- You do not need "Federal Shipping" to display in the results

SELECT 
S.ShipperID, 
S.CompanyName,
O.ShipName,
O.ShipAddress
FROM shippers AS S
JOIN orders AS O
ON S.ShipperID = O.ShipVia
HAVING S.ShipperID = 3 
ORDER BY ShipName;

-- What are the order ids of the orders that included "Sasquatch Ale"?
-- HINT: Find the product id of "Sasquatch Ale" in a subquery and then use that value
-- to find the matching orders from the `order details` table.
-- Your final results only need to display OrderID, but you may find it helpful to include
-- additional columns as you work on creating the query to better understand how the
-- query is working

-- SUBQUERY
-- SELECT 
-- ProductID,
-- ProductName
-- FROM products
-- WHERE ProductName = "Sasquatch Ale"; 

SELECT
    OrderID
FROM `order details`
WHERE ProductID = (
    SELECT ProductID
    FROM Products
    WHERE ProductName = 'Sasquatch Ale'
);

-- What is the name of the employee that sold order 10266?

SELECT 
O.OrderID, 
O.EmployeeID  
FROM Orders AS O 
JOIN Employees AS E 
ON O.EmployeeID = E.EmployeeID  
WHERE O.OrderID = "10266";


-- What is the name of the customer that bought order 10266?
SELECT 
O.OrderID, 
O.CustomerID,
C.ContactName
FROM Orders AS O 
JOIN Customers AS C 
ON O.CustomerID = C.CustomerID
WHERE O.OrderID = "10266";


