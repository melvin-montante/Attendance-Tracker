This project aims to create and export a data that can be used by Laguna employees to easily check their punch ins and outs at work using a fingerprint scanner, and also by employers to analyze attendace of employees. A raw data is downloaded from the fingerprint scanner that captures the daily punch ins and outs at work.

The code "laguna_attendance.py" uses data wrangling techniques to get an output of usable format to analyze attendance record of Laguna employees. The output of this code "output_grouped.xlsx" is an excel file containing separate sheets for each employee.

**INPUTs:**


**Input 1:** The raw data "biometric_punch.dat" lists all punch ins and punch outs of Laguna employees at work and can be downloaded from the biometrics fingerprint scanner which monitors their attendance.
This raw data must be cleaned and transformed into an insightful data where employees can check and analyze their punch ins and outs at work.

*Important columns in the raw dataset:*

First Column - this contains the ID number of the employees

Second Column - this contains the date and time of punch of the employees

Fourth Column - categorical as: 0 - "CHECKIN", 1 - "CHECKOUT", 2 - "BREAKOUT", 3 - "BREAKIN", 4, and 5 - "UNKNOWN"

**Input 2:** The raw data "raw.csv" is created and transformed from "biometric_punch.dat", converting .dat file into .csv file. Note that when the downloaded raw data from scanner is updated, please rename and convert the file to "raw.csv" so the code will not return an error.

**Input 3:** The raw data "user_id.csv" contains the employees name and ID numbers that is merged with "raw_converted.csv". If employee count is updated, download and rename file to "user_id.csv" so the code will not return an error.


**OUTPUTS:**


**Output 1:** The output file "raw_converted.csv" is the converted data of Input 2.

The columns of Input 2 are transformed to a usable format.

Output 1 "raw_converted" will be an input data that can be shaped and finally exported to the final output (Output 2)


**Output 2:** The output of this project "output_grouped.xlsx" is an excel file containing separate sheets for each employee.
This file can be used by employees and employers to analyze attendance record at work.


The output file can be modified by replacing the desired dates of attendace in the code. See line 49 . The current code filters date from October onwards.
