Q1./*Create table with following specifications
•	log_id: A primary key with SERIAL key to uniquely identify each log entry.
•	machine_id: The ID of the machine.
•	production_date: The date of production.
•	production_shift: The shift during which production took place (e.g., 'Morning', 'Evening').
•	products_produced: The number of products produced during the shift.
•	defects: The number of defective products.
•	runtime: The total runtime of the machine during the shift in hours.
Enter the following data
(1, '2024-06-01', 'Morning', 500, 5, 8.0),(1, '2024-06-01', 'Evening', 450, 3, 7.5),
(2, '2024-06-01', 'Morning', 480, 2, 7.8), (2, '2024-06-01', 'Evening', 470, 4, 8.1),
(3, '2024-06-01', 'Morning', 510, 6, 8.2), (3, '2024-06-01', 'Evening', 520, 1, 7.9), 
(1, '2024-06-02', 'Morning', 490, 3, 8.0), (1, '2024-06-02', 'Evening', 460, 2, 7.6), 
(2, '2024-06-02', 'Morning', 475, 1, 7.9),(2, '2024-06-02', 'Evening', 465, 5, 8.3),
(3, '2024-06-02', 'Morning', 505, 4, 8.0), (3, '2024-06-02', 'Evening', 515, 3, 8.2);
In Manufacturers monitor production data to ensure efficient operations and quality control,
identify machines with the highest defect rates and their average runtimes.
*/
drop table company
create table company(
	 log_id SERIAL PRIMARY KEY,
	 machine_id INT,
	 production_date date,
	 production_shift VARCHAR(10) NOT NULL,
	 products_produced INT,
	 defects INT ,
	 runtime INT 
	)

select  * from company

insert into company ( machine_id,production_date,production_shift,products_produced,defects,runtime)
values(1, '2024-06-01', 'Morning', 500, 5, 8.0),
	(1, '2024-06-01', 'Evening', 450, 3, 7.5),
    (2, '2024-06-01', 'Morning', 480, 2, 7.8),
	(2, '2024-06-01', 'Evening', 470, 4, 8.1),
(3, '2024-06-01', 'Morning', 510, 6, 8.2), 
	(3, '2024-06-01', 'Evening', 520, 1, 7.9), 
(1, '2024-06-02', 'Morning', 490, 3, 8.0),
	(1, '2024-06-02', 'Evening', 460, 2, 7.6), 
(2, '2024-06-02', 'Morning', 475, 1, 7.9),
	(2, '2024-06-02', 'Evening', 465, 5, 8.3),
(3, '2024-06-02', 'Morning', 505, 4, 8.0),
	(3, '2024-06-02', 'Evening', 515, 3, 8.2);
	
select machine_id from company
where defects = (select max(defects) from company) AND
runtime = (select avg(runtime) from company)



Assignment-2
	/*
Create table with following specifications
•	grade_id: A primary key with auto-increment to uniquely identify each grade entry.
•	student_id: The ID of the student.
•	course_id: The ID of the course.
•	grade: The grade received by the student.
•	grade_date: The date when the grade was recorded.
Insert following values
(1, 101, 85.5, '2024-01-15'), (1, 102, 78.0, '2024-02-20'), 
(2, 101, 92.0, '2024-01-15'), (2, 103, 88.5, '2024-03-10'), 
(3, 102, 74.0, '2024-02-20'), (3, 103, 81.5, '2024-03-10'),
(4, 101, 67.0, '2024-01-15'), (4, 104, 90.0, '2024-04-05'), 
(5, 102, 85.0, '2024-02-20'), (5, 104, 87.0, '2024-04-05');
Educational institutions track student performance to provide targeted support and interventions.
identify students with an average grade below a passing threshold in their courses
*/


create table student (
	grade_id SERIAL PRIMARY KEY,
	student_id INT,
	course_id INT,
	grade FLOAT,
	grade_date DATE
)
select * from student

insert  into student (student_id,course_id,grade,grade_date)
values 
	(1, 101, 85.5, '2024-01-15'), 
	(1, 102, 78.0, '2024-02-20'),
	(2, 101, 92.0, '2024-01-15'), 
	(2, 103, 88.5, '2024-03-10'),
	(3, 102, 74.0, '2024-02-20'), 
	(3, 103, 81.5, '2024-03-10'), 
	(4, 101, 67.0, '2024-01-15'), 
	(4, 104, 90.0, '2024-04-05'), 
	(5, 102, 85.0, '2024-02-20'), 
	(5, 104, 87.0, '2024-04-05')

select* from 




Assignment-3
	/*
Create table with following specifications
Creation:
•	customer_id: A primary key with auto-increment to uniquely identify each customer.
•	first_name: The first name of the customer.
•	last_name: The last name of the customer.
•	email: The email address of the customer.
•	phone_number: The phone number of the customer.
•	address: The street address of the customer.
•	city: The city where the customer lives.
•	state: The state where the customer lives.
•	zip_code: The postal code of the customer's address.
•	plan_id: The ID of the customer's telecom plan.
•	last_call_date: The date of the customer's last call.
Insert following values
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St', 'Springfield', 'IL', '62701', 1, '2024-06-01'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St', 'Springfield', 'IL', '62701', 2, '2024-05-15'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '789 Pine St', 'Shelbyville', 'IL', '62565', 3, '2024-04-20'),
('Bob', 'Brown', 'bob.brown@example.com', '444-555-6666', '101 Maple St', 'Capital City', 'IL', '62702', 1, '2024-06-10'),
('Charlie', 'Davis', 'charlie.davis@example.com', '333-444-5555', '202 Cedar St', 'Springfield', 'IL', '62701', 2, '2024-03-30'), 
('Diana', 'Evans', 'diana.evans@example.com', '222-333-4444', '303 Birch St', 'Shelbyville', 'IL', '62565', 3, '2024-06-20'), 
('Ethan', 'Foster', 'ethan.foster@example.com', '111-222-3333', '404 Spruce St', 'Capital City', 'IL', '62702', 1, '2024-02-14'), 
('Fiona', 'Garcia', 'fiona.garcia@example.com', '999-888-7777', '505 Ash St', 'Springfield', 'IL', '62701', 2, '2024-05-05'),
('George', 'Harris', 'george.harris@example.com', '888-777-6666', '606 Walnut St', 'Shelbyville', 'IL', '62565', 3, '2024-01-25'), 
('Hannah', 'Irvine', 'hannah.irvine@example.com', '777-666-5555', '707 Hickory St', 'Capital City', 'IL', '62702', 1, '2024-06-22');

Telecom companies analyze customer data to identify patterns that indicate potential churn.
categorizes customers based on their activity levels, indicating their risk of churn.*/

create table telecom(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	email VARCHAR(50),
	phone_number BIGINT,
	address VARCHAR(50),
	city VARCHAR(50),
	state VARCHAR(50),
	zip_code INT,
	plan_id INT,
	last_call_date DATE
)




