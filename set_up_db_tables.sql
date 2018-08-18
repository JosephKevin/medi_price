-- data base schema
create database medical_data;

-- raw data table
create table medical_data.raw_data (
`DRG Definition` varchar(250),
`Provider Id` int,
`Provider Name` varchar(250),
`Provider Street Address` varchar(500),
`Provider City` varchar(500),
`Provider State` varchar(500),
`Provider Zip Code` int,
`Hospital Referral Region Description` varchar(500),
 `Total Discharges` int,
 `Average Covered Charges` int,
 `Average Total Payments` int,
`Average Medicare Payments` int
);

-- loading raw data
LOAD DATA LOCAL INFILE '/Users/joseph/Downloads/Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv'
INTO TABLE medical_data.raw_data FIELDS TERMINATED BY ','
ENCLOSED BY '"'
IGNORE 1 LINES;

-- create predicted value table
create table medical_data.price_prediction (
`DRG Definition` varchar(250),
`Provider State` varchar(500),
`Average Total Payments` int );
