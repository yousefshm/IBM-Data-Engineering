# Relational Database Design & Implementation Project

This project is part of the **IBM Data Engineering Professional Certificate** and represents a hands-on implementation of core relational database concepts.

The objective of this project is to design and implement a centralized relational database system for a fictional coffee shop chain aiming to expand its operations.  
Using **PostgreSQL**, the project covers the complete database design lifecycle — from identifying entities and attributes, to normalization, relationship modeling, and data loading across multiple RDBMS platforms.

---

## 🧠 Project Scenario

A New York–based coffee shop chain plans to expand nationally and requires a modernized data infrastructure to support operational efficiency and data-driven decision-making.

The company’s data is currently scattered across multiple sources, including:
- Spreadsheets
- Point-of-sale (POS) systems
- Supplier databases
- Customer management systems

As a data engineer, the task is to design a **central relational database** that integrates these data sources into a structured and scalable system.

---

## 🛠 Tools & Technologies

- **PostgreSQL** — primary database system (design & implementation)
- **MySQL** — target system for data export and integration
- **pgAdmin** — ERD design and database management
- **SQL** — schema creation, data manipulation, and views

---

## 📋 Project Tasks & Implementation

### 🔹 Task 1: Identify Entities
Reviewed sample data from multiple sources and identified key entities required for the centralized database.

📸 *Screenshot:* `Task1.png`

---

### 🔹 Task 2: Identify Attributes
Defined attributes for the **sales transaction** entity based on POS system data.

📸 *Screenshot:* `Task2.png`

---

### 🔹 Task 3: Create an Entity Relationship Diagram (ERD)
Designed an initial ERD in pgAdmin, defining tables and data types for:
- Sales transactions
- Products

📸 *Screenshots:*  
- `Task3A.png`  
- `Task3B.png`

---

### 🔹 Task 4: Normalize Tables
Normalized the database design to **Second Normal Form (2NF)** by:
- Splitting sales transaction details into a separate table
- Separating product type information to reduce redundancy

📸 *Screenshots:*  
- `Task4A.png`  
- `Task4B.png`

---

### 🔹 Task 5: Define Keys and Relationships
Defined:
- Primary keys for each table
- Relationships between tables:
  - Sales transactions ↔ sales details
  - Sales details ↔ products
  - Products ↔ product types

📸 *Screenshots:*  
- `Task5A.png`  
- `Task5B.png`

---

### 🔹 Task 6: Create Database Objects & Load Data
- Generated SQL schema from the ERD
- Executed schema creation in PostgreSQL
- Loaded sample data into the database
- Verified table creation and data insertion

📸 *Screenshots:*  
- `Task6A.png`  
- `Task6B.png`

---

### 🔹 Task 7: Create a View & Export Data
Created a PostgreSQL **view** to extract staff and location data (excluding executive roles) and exported the results to CSV.

📸 *Screenshot:* `Task7.png`

---

### 🔹 Task 8: Create a Materialized View
Created a **materialized view** combining product and product category data, then exported it to CSV for downstream use.

📸 *Screenshot:* `Task8.png`

---

### 🔹 Task 9: Import Data into MySQL
Imported staff location data into a MySQL database using phpMyAdmin and validated the imported records.

📸 *Screenshot:* `Task9.png`

---

### 🔹 Task 10: Import Product Data into MySQL
Imported product data from the materialized view into a MySQL database for marketing analytics.

📸 *Screenshot:* `Task10.png`

---

## 🎯 Key Learning Outcomes

- Relational database design from real-world requirements
- Entity and attribute identification
- Table normalization and schema optimization
- ERD-based schema generation
- Cross-database data export and integration
- Practical PostgreSQL implementation

---

## 📌 Notes

- All tasks were implemented using **PostgreSQL** as the primary RDBMS.
- Screenshots included in this repository document each step of the implementation.
- This project focuses on **practical database engineering**, not theoretical modeling only.

