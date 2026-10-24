CREATE DATABASE IF NOT EXISTS attendance_db;
USE attendance_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    dob DATE,
    password VARCHAR(200) NOT NULL,
    role ENUM('admin','student') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY unique_attendance (student_id, date)
) ENGINE=InnoDB;

-- Sample data (one admin, one student)
INSERT INTO users (username, email, password, role) VALUES
('AdminUser', 'admin@example.com',
 'pbkdf2:sha256:150000$adj4F9xgob6lcro9$a21263798bf2ee27004b43022db28ec3db31ac1693785596d3485064452eb0cf', 'admin'),




