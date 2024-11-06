This project aims to create and export a data that can be used by Laguna employees to easily check their punch ins and outs at work using a fingerprint scanner, and also by employers to analyze attendace of employees. A raw data is downloaded from the fingerprint scanner that captures the daily punch ins and outs at work.

The code "laguna_attendance.py" uses data wrangling techniques to get an output of usable format to analyze attendance record of Laguna employees. The output of this code "grouped_ids_output.xlsx" is an excel file containing separate sheets for each employee.

INPUTs:


Input 1

  The raw data "biometric_punch.dat" lists all punch ins and punch outs of Laguna employees at work and can be downloaded from the biometrics fingerprint scanner which monitors their attendance.
This raw data must be cleaned and transformed into an insightful data where employees can check and analyze their punch ins and outs at work.

Important columns in the raw dataset:
First Column - this contains the ID number of the employees
Second Column - this contains the date and time of punch of the employees
Fourth Column - categorical as: 0 - "CHECKIN", 1 - "CHECKOUT", 2 - "BREAKOUT", 3 - "BREAKIN", 4, and 5 - "UNKNOWN"

Input 2

  The raw data "laguna_bio_info.csv" is created and transformed from "biometric_punch.dat", converting .dat file into .csv file.

Input 3

  The raw data "user_id.csv" contains the employees name and ID numbers that is merged with "laguna_info.csv".


OUTPUT:

The output of this project "grouped_ids_output.xlsx" is an excel file containing separate sheets for each employee. This file can be used by employees and employers to analyze attendance record at work.
