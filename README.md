Banking Application Using Streamlit

OVERVIEW :

This project is a simple, interactive Banking Application built using Streamlit for the user interface and MySQL as the database. It allows users to perform basic banking operations such as account creation, login, deposits, withdrawals, and balance inquiries in a secure and user-friendly environment.

The application is designed to demonstrate the integration of Python with a relational database, showcasing robust functionality and a clean UI for a seamless user experience.

FEATURES :- Account Creation: Users can create a new account by entering their name, initial deposit amount, PIN, and password.

Secure Login: Users can log in using their account number and password, with validation to ensure data security.

Deposit Money: Users can deposit money into their account by entering their PIN and the amount.

Withdraw Money: Users can withdraw funds, ensuring sufficient balance and valid PIN entry.

Check Account Balance: Users can securely view their account balance by providing their PIN.

TECHNOLOGY USED :- Frontend: Streamlit - Python-based library for creating interactive web applications. Backend Database: MySQL - For storing user account details and transaction data. Programming Language: Python.

Installation and Setup :- Prerequisites :

Install Python (3.8 or higher). Download Python
Install MySQL and set up a database. Download MySQL
Install required Python libraries: pip install streamlit mysql-connector-python
Database Setup : Create a database named mybank in MySQL:

CREATE DATABASE mybank;
Create a table for storing user account details:

CREATE TABLE customer_ac ( ac_no INT AUTO_INCREMENT PRIMARY KEY, cname VARCHAR(255) NOT NULL, balance FLOAT NOT NULL, pin INT NOT NULL, password VARCHAR(255) NOT NULL );
Navigate to the project directory:

cd streamlit-banking-app Run the application:
streamlit run app.py
Open the URL provided in the terminal to access the application.
How to Use :- 1.Sign Up:

Enter your details to create a new account.
A minimum balance of 1000 is required. 2.Login:
Use your account number and password to log in. 3.Banking Operations:
Choose an option (Deposit, Withdraw, Check Balance) from the radio button menu.
Follow the instructions to complete your operation.
Future Improvements :-

Add transaction history for each user.
Implement a password recovery feature.
Enhance UI with additional visuals.
Add admin functionality for managing accounts.
