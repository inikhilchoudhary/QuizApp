-- Create the QUIZBEE database
CREATE DATABASE QUIZBEE;
USE QUIZBEE;

-- Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'teacher', 'student') NOT NULL,
    subject VARCHAR(255) DEFAULT NULL -- This column is relevant only for students and can be NULL for others
);

-- Create the teachers table
CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create the students table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    subject VARCHAR(255) DEFAULT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a trigger to insert into teachers or students table when a user is added
DELIMITER $$
CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    IF NEW.role = 'teacher' THEN
        INSERT INTO teachers (name, username, email, password, user_id) 
        VALUES (NEW.name, NEW.username, NEW.email, NEW.password, NEW.id);
    ELSEIF NEW.role = 'student' THEN
        INSERT INTO students (name, username, email, password, subject, user_id) 
        VALUES (NEW.name, NEW.username, NEW.email, NEW.password, NEW.subject, NEW.id);
    END IF;
END$$
DELIMITER ;

