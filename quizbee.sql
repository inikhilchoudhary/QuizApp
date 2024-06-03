USE QUIZBEE;
SELECT * FROM USERS;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'teacher', 'student') NOT NULL,
    subject VARCHAR(255) DEFAULT NULL -- This column is relevant only for students and can be NULL for others
);
INSERT INTO users (name, username, email, password, role) VALUES ('Admin', 'admin', 'admin@example.com', 'admin_password', 'admin');
INSERT INTO users (name, username, email, password, role) VALUES ('Teacher1', 'teacher1', 'teacher1@example.com', 'teacher1_password', 'teacher');
select * from users;

SET SQL_SAFE_UPDATES=0;              

UPDATE users
SET password='t'
WHERE password='teacher1_password';
