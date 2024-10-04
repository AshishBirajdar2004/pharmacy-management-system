create database pharmeasy;
use pharmeasy;

CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);
ALTER TABLE categories AUTO_INCREMENT=101;
INSERT INTO Categories (category_name)
VALUES 
('Antibiotic'),
('Pain Reliever'),
('Antiseptic'),
('Antacid'),
('Vaccine'),
('Anti-inflammatory'),
('Antifungal'),
('Antihistamine'),
('Antiviral'),
('Supplements');
select * from categories;


CREATE TABLE Medicines (
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    medicine_name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    expiry_date DATE,
    quantity INT DEFAULT 0,
    price DECIMAL(10, 2),
    category_id INT,
    CONSTRAINT fk_category
        FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);
ALTER TABLE Medicines AUTO_INCREMENT=201;
INSERT INTO Medicines (medicine_name, manufacturer, category_id, expiry_date, quantity, price)
VALUES
('Amoxicillin', 'Pfizer', 101, '2025-05-15', 100, 10.50),
('Ibuprofen', 'Johnson & Johnson', 102, '2024-11-30', 200, 5.25),
('Aspirin', 'Bayer', 102, '2026-02-20', 150, 3.75),
('Loratadine', 'Merck', 103, '2025-09-12', 120, 8.00),
('Omeprazole', 'AstraZeneca', 104, '2025-03-10', 180, 6.50),
('Metformin', 'Sun Pharma', 105, '2024-12-01', 130, 12.00),
('Salbutamol', 'GlaxoSmithKline', 106, '2024-10-25', 50, 7.80),
('Clotrimazole', 'Novartis', 107, '2025-07-30', 70, 9.10),
('Paracetamol', 'Cipla', 102, '2026-01-19', 300, 2.50),
('Atorvastatin', 'Ranbaxy', 101, '2025-08-05', 90, 11.40);
select * from Medicines;


CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(15)
);
ALTER TABLE Customers AUTO_INCREMENT=301;
INSERT INTO Customers (customer_name, phone_number, address) VALUES
('Alice Johnson', '555-0123', '123 Maple St, Springfield'),
('Bob Smith', '555-0456', '456 Oak St, Springfield'),
('Charlie Brown', '555-0789', '789 Pine St, Springfield'),
('David Wilson', '555-1011', '321 Birch St, Springfield'),
('Emma Davis', '555-1213', '654 Cedar St, Springfield'),
('Frank Miller', '555-1415', '987 Elm St, Springfield'),
('Grace Lee', '555-1617', '135 Spruce St, Springfield'),
('Henry Taylor', '555-1819', '246 Willow St, Springfield'),
('Irene Martinez', '555-2021', '369 Aspen St, Springfield'),
('Jack Brown', '555-2223', '482 Fir St, Springfield');
select * from Customers;

CREATE TABLE Prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    medicine_id INT,
    dosage VARCHAR(50),
    frequency  VARCHAR(50),
    prescription_date DATE DEFAULT (CURDATE()),
    CONSTRAINT fk_prescription_customer
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    CONSTRAINT fk_prescription_medicine
        FOREIGN KEY (medicine_id) REFERENCES Medicines(medicine_id)
);
ALTER TABLE Prescriptions AUTO_INCREMENT=401;
INSERT INTO Prescriptions (customer_id, medicine_id, dosage, frequency) VALUES
(301, 202, '500 mg', 'Twice daily'),
(302, 204, '250 mg', 'Once daily'),
(303, 201, '100 mg', 'Three times a day'),
(301, 203, '50 mg', 'Once daily'),
(304, 205, '10 mg', 'Twice daily'),
(305, 206, '500 mg', 'Once daily'),
(302, 207, '20 mg', 'Once every 12 hours'),
(306, 208, '250 mg', 'Twice daily'),
(307, 209, '750 mg', 'Once daily'),
(308, 210, '150 mg', 'Three times a day');
select * from prescriptions;

CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    medicine_id INT,
    quantity_sold INT,
    sale_date DATE DEFAULT (CURDATE()),
    total_price DECIMAL(10, 2),
    discount_percentage DECIMAL(5, 2),
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    CONSTRAINT fk_medicine
        FOREIGN KEY (medicine_id) REFERENCES Medicines(medicine_id)
);
ALTER TABLE sales AUTO_INCREMENT=501;
INSERT INTO Sales (customer_id, medicine_id, quantity_sold, total_price, discount_percentage)
VALUES 
(301, 201, 2, 100.00, 0),   -- John bought 2 Paracetamol for 100
(302, 202, 1, 120.00, 0),   -- Jane bought 1 Amoxicillin for 120
(303, 203, 3, 90.00, 10.00), -- Alice bought 3 Aspirin, 10% discount
(304, 204, 1, 150.00, 5.00), -- Bob bought 1 Ibuprofen, 5% discount
(305, 205, 4, 200.00, 0),   -- Charlie bought 4 Metformin for 200
(306, 206, 2, 140.00, 5.00), -- David bought 2 Amoxicillin, 5% discount
(307, 207, 5, 180.00, 0),   -- Emily bought 5 Atorvastatin for 180
(308, 208, 6, 250.00, 0),   -- Frank bought 6 Losartan for 250
(309, 209, 2, 120.00, 0),   -- Grace bought 2 Amoxicillin for 120
(310, 210, 7, 220.00, 0); -- Helen bought 7 Simvastatin for 220
select * from sales;

