CREATE DATABASE doc_for_all;
USE doc_for_all;

CREATE TABLE Hospital(
    Id INTEGER AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Phone_no VARCHAR(14) UNIQUE NOT NULL,
    Street VARCHAR(20) NOT NULL,
    City VARCHAR(20) NOT NULL,
    State VARCHAR(20) NOT NULL,
    Pincode VARCHAR(6) NOT NULL,
    PRIMARY KEY(Id)
);

CREATE TABLE Doctor(
    Id INTEGER AUTO_INCREMENT PRIMARY KEY,
    Hospital_Id INTEGER DEFAULT NULL,
    Street VARCHAR(20) NOT NULL,
    City VARCHAR(20) NOT NULL,
    State VARCHAR(20) NOT NULL,
    Pincode VARCHAR(6) NOT NULL,
    F_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    Qualification VARCHAR(50) NOT NULL,
    Phone_no VARCHAR(14) UNIQUE NOT NULL,
    Specialization VARCHAR(100) NOT NULL
);
    
    CREATE TABLE Patient (
    Id INTEGER AUTO_INCREMENT PRIMARY KEY,
    F_Name VARCHAR(20) NOT NULL,
    M_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    Phone_No VARCHAR(14) UNIQUE NOT NULL,
    DOB DATE,
    Street VARCHAR(20) NOT NULL,
    City VARCHAR(20) NOT NULL,
    State VARCHAR(20) NOT NULL,
    Pincode VARCHAR(6) NOT NULL
);
    CREATE TABLE Patient_Records (
    Id INTEGER AUTO_INCREMENT,
    Patient_Id INTEGER NOT NULL,
    Doctor_Id INTEGER NOT NULL,
    P_Diagnostics VARCHAR(100) NOT NULL,
    FOREIGN KEY(Patient_Id) REFERENCES Patient(Id),
    FOREIGN KEY (Doctor_Id) REFERENCES Doctor(Id),
    UNIQUE (Patient_Id,Doctor_Id),
    PRIMARY KEY(Id)
    );

    CREATE TABLE Appointments(
    Id INTEGER AUTO_INCREMENT PRIMARY KEY,
    Patient_Records_Id INTEGER,
    Date_Of_Appointment DATE,
    Medication INTEGER,
    Medicines VARCHAR(100),
    Fee_Paid FLOAT(6,2),
    Ratings INTEGER,
    FOREIGN KEY(Patient_Records_Id) REFERENCES Patient_Records(Id)
);
    


 # Address CONCAT_WS(',',State,City,Street,Pincode),
 #  Name CONCAT_WS(' ',F_Name,M_Name,L_Name) UNIQUE,
 # Age YEAR(CURDATE())-YEAR(DOB);