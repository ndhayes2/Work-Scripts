-- CREATE TABLE Conveyance (
--     "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--     "Length (m)" REAL,
--     "Lift or Drop (m)" REAL,
--     "Belt Width (mm)" REAL,
--     "Design Load (TPH)" REAL,
--     "Vendor" TEXT,
--     "Model" TEXT,
--     "Purchase Date (MM-DD-YYYY)" TEXT,
--     "Price" REAL,
--     "Quantity Purchased" INTEGER
-- );

-- CREATE TABLE Pumps (
--     "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--     "HP" REAL,
--     "Flow Rate (GPM)" REAL,
--     "Method of Action" TEXT,
--     "Vendor" TEXT,
--     "Model" TEXT,
--     "Purchase Date (MM-DD-YYYY)" TEXT,
--     "Price" REAL,
--     "Quantity Purchased" INTEGER
-- );

-- CREATE TABLE Crushing (
--     "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--     "Throughput (TPH)" REAL,
--     "Electricity Requirements (kW)" REAL,
--     "Initial Size (sqft)" REAL,
--     "Final Size (sqft)" REAL,
--     "Vendor" TEXT,
--     "Model" TEXT,
--     "Purchase Date (MM-DD-YYYY)" TEXT,
--     "Price" REAL,
--     "Quantity Purchased" INTEGER 
--     );

-- CREATE TABLE Grinding (
--     "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--     "Throughput (TPH)" REAL,
--     "Electricity Requirements (kW)" REAL,
--     "Length" REAL,
--     "Vendor" TEXT,
--     "Model" TEXT,
--     "Purchase Date (MM-DD-YYYY)" TEXT,
--     "Price" REAL,
--     "Quantity Purchased" INTEGER);

-- CREATE TABLE Flotation (
--     "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--     "Method of Action" TEXT,
--     "Volume (ft3)" REAL,
--     "Throughput" REAL,
--     "Size of Bank" INTEGER,
--     "Vendor" TEXT,
--     "Model" TEXT,
--     "Purchase Date (MM-DD-YYYY)" TEXT,
--     "Price" REAL,
--     "Quantity Purchased" INTEGER);

-- INSERT INTO Flotation ("Method of Action", "Volume (ft3)", "Throughput", "Size of Bank", "Vendor", "Model", "Purchase Date (MM-DD-YYYY)", "Price", "Quantity Purchased") 
-- VALUES ('TEST', 155, 1500, 7, 'TEST', 'TEST', '2019-07-17', 220000, 1);

SELECT * FROM Flotation