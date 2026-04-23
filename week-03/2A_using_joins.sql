USE northwind;

-- Create a single query to list the product id, product name,unit price and category
-- name of all products. Order by category name and within that, by product name.
    
SELECT Prd.ProductID,
       Prd.ProductName,
       Prd.CategoryID,
       Prd.UnitPrice,
       Cat.CategoryID,
       Cat.CategoryName
FROM Products Prd
INNER JOIN Categories Cat
    ON Cat.CategoryID = Prd.CategoryID
ORDER BY Cat.CategoryName asc, Prd.ProductName asc; 

-- Create a single query to list the product id, product name, unit price and supplier
-- name of all products that cost more than $75. Order by product name

SELECT 
    Prd.ProductID, 
    Prd.ProductName, 
    Prd.UnitPrice, 
    Supp.SupplierID,
    Supp.CompanyName
FROM Products Prd
INNER JOIN Suppliers Supp
    ON Supp.SupplierID = Prd.SupplierID
WHERE Prd.UnitPrice >= 75
ORDER BY Prd.ProductName;

-- Create a single query to list the product id, product name, unit price, category name,   
-- and supplier name of every product. Order by product name.

SELECT 
    Prd.ProductID, 
    Prd.ProductName, 
    Prd.UnitPrice, 
    Prd.CategoryID,
    Supp.SupplierID,
    Supp.CompanyName,
    Cat.CategoryName
FROM Products Prd
INNER JOIN Suppliers Supp
	ON Supp.SupplierID = Prd.SupplierID
INNER JOIN Categories Cat
    ON Prd.CategoryID = Cat.CategoryID
ORDER BY Prd.ProductName;

-- Create a single query to list the order id, ship name, ship address, and shipping 
-- Company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
-- Shipped to. 

SELECT 
Ord.OrderID,
Ord.ShipVia,
Ord.ShipName,
Ord.ShipAddress,
Ord.ShipCountry,
Ord.ShipName,
Ship.ShipperID,
Ship.CompanyName
FROM Orders Ord
INNER JOIN Shippers Ship
	ON Ord.ShipVia=Ship.ShipperID
    WHERE Ord.Shipcountry = "Germany"
ORDER BY Ship.CompanyName, 	
	Ord.ShipName; 

-- Start from the same query as above (#4), but omit OrderID and add logic to group by
-- Ship name, with a count of how many orders were shipped for that ship name
-- REVIST NEED TO REVIEW -- 

-- Create a single query to list the order id, order date, ship name, ship address of all
-- orders that included Sasquatch Ale.

SELECT 
Ord.OrderID,
Ord.OrderDate,
Ord.ShipName,
Ord.ShipAddress,
Det.ProductID,
Prd.ProductName,
Prd.ProductID
FROM Orders Ord
INNER JOIN `order details` det
ON Ord.OrderID = Det.OrderID
INNER JOIN Products Prd
    ON Det.ProductID = Prd.ProductID
WHERE Prd.ProductName = 'Sasquatch Ale';

-- 