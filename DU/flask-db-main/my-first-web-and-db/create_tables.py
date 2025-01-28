"""
CREATE TABLE Instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100)
);


CREATE TABLE Classes (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    instructor_id INT,
    class_time TIME,
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);


CREATE TABLE Visitors (
    visitor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    phone_provider VARCHAR(50),
    last_visited DATE
);


CREATE TABLE ClassRegistrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    class_id INT,
    visitor_id INT,
    date DATE,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id),
    FOREIGN KEY (visitor_id) REFERENCES Visitors(visitor_id)
);


"""