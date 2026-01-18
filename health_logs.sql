CREATE DATABASE IF NOT EXISTS HealthPulse;
USE HealthPulse;

CREATE TABLE service_health (
    id INT PRIMARY KEY AUTO_INCREMENT,
    service_name VARCHAR(100),
    status VARCHAR(20),
    response_time_ms INT,
    check_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data for history
INSERT INTO service_health (service_name, status, response_time_ms) 
VALUES ('Claims-API', 'Online', 120), ('Enrollment-DB', 'Online', 45);