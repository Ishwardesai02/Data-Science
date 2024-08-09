1.	Write a SQL statement to create a simple table countries, including columns 
	country_id,country_name and region_id which already exist.

create table countries(
	 country_id INT Unique Primary key,
	  country_name varchar(50) ,
	 region_id INT unique 
)



2.	Create the two tables Sales and products and insert some sample data into them.
Sales table columns: 
sale_id	product_id	quantity_sold	sale_date	total_price

Products table columns:
product_id	product_name	category	unit_price

Filter the Sales table to show only sales with a total_price greater than $100.


create table Sales(
	sale_id INT Primary Key ,
	product_id INT ,
	quantity_sold INT,
	sale_date Date ,
	total_price INT 
)

create table Products(
	products_id INT primary key, 
	product_name varchar(50),
	category varchar(20),
	unit_price INT 
)

insert into Sales(
	sale_id,
	product_id,
	quantity_sold,
	sale_date,
	total_price
	)
values
(
	'1',
	'11',
	'200',
	'2024-06-03',
	'199'
	
)

insert into Sales(
	sale_id,
	product_id,
	quantity_sold,
	sale_date,
	total_price
	)
values
(
	'2',
	'12',
	'201',
	'2023-06-04',
	'99'
	
)

insert into Sales(
	sale_id,
	product_id,
	quantity_sold,
	sale_date,
	total_price
	)
values
(
	'3',
	'15',
	'204',
	'2023-07-08',
	'89'
	
)

insert into Sales(
	sale_id,
	product_id,
	quantity_sold,
	sale_date,
	total_price
	)
values
(
	'4',
	'16',
	'2005',
	'2021-08-09',
	'149'
	
)

select * from Sales 
where total_price>100


3.	Retrieve the total_price of all sales, rounding the values to two decimal places.


	create table sale(
	sale_id INT Primary Key ,
	product_id INT ,
	quantity_sold INT,
	total_price Float 
)

insert into sale(
	sale_id,
	product_id,
	quantity_sold,
	total_price
	)
values
(
	'6',
	'16',
	'205',
	'149.9'
	
)

insert into sale(
	sale_id,
	product_id,
	quantity_sold,
	total_price
	)
values
(
	'7',
	'14',
	'207',
	'139.9'
	
)

insert into sale(
	sale_id,
	product_id,
	quantity_sold,
	total_price
	)
values
(
	'8',
	'15',
	'208',
	'129.9'
	
)

select total_price,
case total_price
	when 149.9 then 150
	when 139.9 then 140
	when 129.9 then 130

End as round_off
from sale

select round(total_price) from sale




5.	Retrieve the product_name and category from the Products table, ordering the results by category in ascending order.

	
	

	




	




	