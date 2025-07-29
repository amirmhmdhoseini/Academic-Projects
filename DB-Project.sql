CREATE DATABASE SportsClubDB;
USE SportsClubDB;
CREATE TABLE Member (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    NationalCode CHAR(10) UNIQUE NOT NULL,
    Gender CHAR(1),
    PhoneNumber VARCHAR(15) UNIQUE,
    DateOfBirth DATE,
    Address VARCHAR(255),
    MembershipStatus VARCHAR(20)
);
CREATE TABLE Coach (
    CoachID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Specialty VARCHAR(100),
    ExperienceYears INT,
    PhoneNumber VARCHAR(15) UNIQUE,
    Email VARCHAR(100) UNIQUE,
    HireDate DATE
);
CREATE TABLE Facility (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Type VARCHAR(50),
    Location VARCHAR(255),
    Capacity INT,
    Status VARCHAR(50)
);
CREATE TABLE SportClass (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,
    ClassName VARCHAR(100) NOT NULL,
    Level VARCHAR(50),
    Capacity INT,
    StartDate DATE,
    EndDate DATE,
    DaysOfWeek VARCHAR(50),
    CoachID INT,
    FOREIGN KEY (CoachID) REFERENCES Coach(CoachID)
);
CREATE TABLE Enrollment (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    ClassID INT,
    EnrollDate DATE,
    PaymentStatus VARCHAR(20),
    AttendanceCount INT,
    IsActive TINYINT(1),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    FOREIGN KEY (ClassID) REFERENCES SportClass(ClassID)
);
CREATE TABLE Payment (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    PaymentType VARCHAR(50),
    Method VARCHAR(50),
    ReceiptNumber VARCHAR(50) UNIQUE,
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
);
CREATE TABLE Schedule (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,
    ClassID INT,
    DayOfWeek VARCHAR(20),
    StartTime TIME,
    EndTime TIME,
    Location VARCHAR(255),
    FacilityID INT,
    FOREIGN KEY (ClassID) REFERENCES SportClass(ClassID),
    FOREIGN KEY (FacilityID) REFERENCES Facility(FacilityID)
);
INSERT INTO Member (FirstName, LastName, NationalCode, Gender, PhoneNumber, DateOfBirth, Address, MembershipStatus)
VALUES
('Ali', 'Ahmadi', '1234567890', 'M', '09121234567', '1990-05-10', 'Tehran', 'Active'),
('Sara', 'Mohammadi', '0987654321', 'F', '09129876543', '1992-08-15', 'Tehran', 'Active'),
('Reza', 'Karimi', '1122334455', 'M', '09121112222', '1988-03-22', 'Mashhad', 'Inactive');

INSERT INTO Coach (FirstName, LastName, Specialty, ExperienceYears, PhoneNumber, Email, HireDate)
VALUES
('Hassan', 'Shirazi', 'Yoga', 5, '09123334455', 'h.shirazi@example.com', '2018-01-10'),
('Mina', 'Rahimi', 'Swimming', 3, '09124445566', 'm.rahimi@example.com', '2020-05-20');

INSERT INTO Facility (Name, Type, Location, Capacity, Status)
VALUES
('Main Gym', 'Gym', 'Building A', 50, 'Open'),
('Pool', 'Swimming Pool', 'Building B', 30, 'Open');

INSERT INTO SportClass (ClassName, Level, Capacity, StartDate, EndDate, DaysOfWeek, CoachID)
VALUES
('Yoga Basics', 'Beginner', 20, '2025-06-01', '2025-08-31', 'Monday,Wednesday,Friday', 1),
('Advanced Swimming', 'Advanced', 15, '2025-06-15', '2025-09-15', 'Tuesday,Thursday', 2);

INSERT INTO Enrollment (MemberID, ClassID, EnrollDate, PaymentStatus, AttendanceCount, IsActive)
VALUES
(1, 1, '2025-05-20', 'Paid', 10, 1),
(2, 1, '2025-05-22', 'Unpaid', 5, 1),
(3, 2, '2025-05-25', 'Paid', 8, 0);

INSERT INTO Payment (MemberID, Amount, PaymentDate, PaymentType, Method, ReceiptNumber)
VALUES
(1, 150.00, '2025-05-20', 'Membership', 'Cash', 'R001'),
(2, 100.00, '2025-05-22', 'Membership', 'Card', 'R002');

INSERT INTO Schedule (ClassID, DayOfWeek, StartTime, EndTime, Location, FacilityID)
VALUES
(1, 'Monday', '09:00:00', '10:00:00', 'Room 1', 1),
(2, 'Tuesday', '15:00:00', '16:30:00', 'Poolside', 2);


USE SportsClubDB;

-- Select first 5 members with specific attributes
SELECT MemberID, FirstName, LastName, NationalCode, MembershipStatus
FROM Member
LIMIT 5;

-- Select all members from Member table
SELECT * FROM Member;

-- Select all coaches from Coach table
SELECT * FROM Coach;

-- Get all sport classes with their assigned coach names
SELECT sc.ClassName, c.FirstName, c.LastName
FROM SportClass sc
JOIN Coach c ON sc.CoachID = c.CoachID;

-- List members enrolled in Yoga class with their names
SELECT m.FirstName, m.LastName, sc.ClassName
FROM Enrollment e
JOIN Member m ON e.MemberID = m.MemberID
JOIN SportClass sc ON e.ClassID = sc.ClassID
WHERE sc.ClassName = 'Yoga';

-- Show payment amounts and dates along with member names by joining Payment and Member tables
SELECT m.FirstName, m.LastName, p.Amount, p.PaymentDate
FROM Payment p
JOIN Member m ON p.MemberID = m.MemberID;

-- Show schedule details with sport class names
SELECT sc.ClassName, s.DayOfWeek, s.StartTime, s.EndTime, s.Location
FROM Schedule s
JOIN SportClass sc ON s.ClassID = sc.ClassID;

-- Select coaches with more than 2 years of experience
SELECT * FROM Coach WHERE ExperienceYears > 2;

-- Select members with active membership status
SELECT * FROM Member WHERE MembershipStatus = 'Active';

-- Count total members enrolled in each sport class
SELECT sc.ClassName, COUNT(e.EnrollmentID) AS TotalMembers
FROM SportClass sc
LEFT JOIN Enrollment e ON sc.ClassID = e.ClassID
GROUP BY sc.ClassName;

-- Select members who have not made any payments yet
SELECT m.FirstName, m.LastName
FROM Member m
LEFT JOIN Payment p ON m.MemberID = p.MemberID
WHERE p.PaymentID IS NULL;

-- Update membership status to 'Inactive' for member with MemberID = 3
UPDATE Member SET MembershipStatus = 'Inactive' WHERE MemberID = 3;

-- Delete sport class named 'Pilates' (commented out for safety)
-- DELETE FROM SportClass WHERE ClassName = 'Pilates';


