/* 
a) This table includes the first and last name of actors and actor id
b) This table includes name of film and brief description
c) Table for film includes information for ActorID and FilmID
d) This query created for rental was hard to read because of the amount of information provided, it includes multiple ID and dates 
e) includes inventory id store id film id and the last time it was updated
f) The tables that are needed would be both rental and inventory the retnal provides insight on rental id and also customer id while the inventory provides film id and inventory id number. 

*/

USE sakila;

SELECT * FROM actor; -- Use to answer QA 
SELECT * FROM film; -- Use to answer QB
SELECT * FROM film_actor; -- Use to answer QC
SELECT film_id FROM film;
SELECT rental_id, rental_date, inventory_id
FROM rental;

