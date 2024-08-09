select count(*) from customer
where First_name LIKE 'J%'


select count(*) from customer
where First_name LIKE 'J%' AND last_name LIKE 'S%'

select * from customer
where First_name LIKE 'J%' AND last_name ILIKE 'j%'

select * from customer
where First_name LIKE '%er%'


select * from customer
where First_name LIKE '%her%'


select * from customer
where First_name LIKE '_her%'

select * from customer
where first_name NOT LIKE '_her%'


select * from customer
where First_name LIKE 'A%'
ORDER BY last_name


select * from customer
where First_name LIKE 'A%' AND last_name NOT LIKE 'B%'
ORDER BY last_name

select count(*) from payment
where amount >5


select count(*) from actor
where first_name LIKE 'P%'

select Count(DISTINCT(district)) from address

select DISTINCT district from address

select count(*) from film
where rating='R' 
AND replacement_cost BETWEEN 5 AND 15

Select count(*) from film
where title LIKE '%Truman%'

--Aggregate Functions 
	
SELECT MIN(replacement_cost) from film

SELECT MAX(replacement_cost) from film

SELECT MIN(replacement_cost) , MAX(replacement_cost) from film

--08/07/2024
	
select customer_id,COUNT(*)
FROM payment 
GROUP BY customer_id
HAVING COUNT(*)>=40;


select customer_id ,SUM(amount)
from payment 
where staff_id=2
GROUP BY customer_id
HAVING SUM(amount)>100;

--Alias AS

select amount as rental_price from payment

SELECT SUM(amount) AS rental_price FROM payment

SELECT COUNT(amount) AS number_of_transactions FROM payment

SELECT COUNT(*) AS number_of_transactions FROM payment

SELECT customer_id,SUM(amount) 
FROM payment 
GROUP BY customer_id

SELECT customer_id,SUM(amount) AS total_spent
FROM payment 
GROUP BY customer_id

SELECT customer_id,SUM(amount) 
FROM payment 
GROUP BY customer_id
HAVING SUM(amount)>100

SELECT customer_id,SUM(amount) AS total_spent
FROM payment 
GROUP BY customer_id
HAVING SUM(amount)>100
 
select customer_id,amount
FROM payment
WHERE amount>2


select * from payment
select * from customer

SELECT payment_id,payment.customer_id,first_name FROM payment
INNER JOIN customer
ON payment.customer_id=customer.customer_id

SELECT payment_id,payment.customer_id,first_name
FROM customer
INNER JOIN payment
ON payment.customer_id=customer.customer_id


SELECT * from customer 
FULL OUTER JOIN payment 
ON customer.customer_id = payment.customer_id


SELECT * from film
select * from inventory

SELECT film.film_id,title,inventory_id
FROM film
LEFT JOIN inventory ON
inventory.film_id=film.film_id

SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory ON 
inventory.film_id=film.film_id
WHERE inventory.film_id IS NULL


SELECT film.film_id,title,inventory_id
FROM film
RIGHT JOIN inventory ON
inventory.film_id=film.film_id

SELECT film.film_id,title,inventory_id
FROM inventory
RIGHT JOIN film ON
inventory.film_id=film.film_id


SELECT film.film_id,title,inventory_id,store_id
FROM film
RIGHT JOIN inventory ON 
inventory.film_id=film.film_id
WHERE inventory.film_id IS NULL


select * from customer

select * from address 
inner join customer
on address.address_id=customer.address_id
where district ='California'



select * from film_actor

select title,first_name,last_name from actor
INNER JOIN film_actor
ON actor.actor_id=film_actor.actor_id
INNER JOIN film
ON film_actor.film_id=film.film_id
where first_name='Nick' AND last_name ='Wahlberg'



select * from payment


--10/07/2024

SELECT customer_id FROM customer

SELECT customer_id,
CASE 
     WHEN(customer_id <= 100) THEN 'PREMIUM'
     WHEN(customer_id BETWEEN 100 AND 200)  THEN 'Plus'
     Else 'Normal'
END AS customer_class
FROM customer


SELECT customer_id,
CASE customer_id
     WHEN 2 THEN 'Winner'
     WHEN 5 THEN 'Second place'
     Else 'Normal'
END AS raffle_results
FROM customer


SELECT rental_rate FROM film

SELECT rental_rate,
CASE rental_rate
    WHEN 4.99 THEN 5
    WHEN 0.99 THEN 1
    WHEN 2.99 THEN 3
    WHEN 3.99 THEN 4
END as round_off
FROM film

SELECT 
SUM(
CASE rental_rate
    WHEN 4.99 THEN 5
    WHEN 0.99 THEN 1
    WHEN 2.99 THEN 3
    WHEN 3.99 THEN 4
	
END )as number_of_bargens
FROM film
    

