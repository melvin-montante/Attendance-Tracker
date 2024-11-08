This project aims to create and export a data that can be used by Laguna employees to easily check their punch ins and outs at work using a fingerprint scanner, and also by employers to analyze attendace of employees. A raw data is downloaded from the fingerprint scanner that captures the daily punch ins and outs at work.

The code "attendance_and_tardiness_tracker.py" uses data wrangling techniques to get an output of usable format to analyze attendance record of Laguna employees. 

**INPUTs:**


**Input 1:** The raw data "biometric_punch.dat" lists all punch ins and punch outs of Laguna employees at work and can be downloaded from the biometrics fingerprint scanner which monitors their attendance.
This raw data must be cleaned and transformed into an insightful data where employees can check and analyze their punch ins and outs at work.

*Important columns in the raw dataset "biometric_punch.dat":*

First Column - this contains the ID number of the employees

Second Column - this contains the date and time of punch of the employees

Fourth Column - categorical as: 0 - "CHECKIN", 1 - "CHECKOUT", 2 - "BREAKOUT", 3 - "BREAKIN", 4, and 5 - "UNKNOWN"


**Input 2:** The raw data "user_id.csv" contains the employees name and ID numbers that is merged with "biometric_punch.dat". 
Note that if employee count is updated, download and rename file to "user_id.csv" so the code will not return an error.


**OUTPUTS:**


**Output 1:** One output of this project "output_grouped.xlsx" is an excel file containing separate sheets for each employee. This shows a structured data of employees' daily punch-ins and punch-outs. This file can be sent to employees for them to check their attendance. It can also be used by employers to analyze absenteeism and tardiness of employees.

**Output 2:** Another output of this project "late_employees.xlsx" is an excel file that shows the tardiness count of each employee, and the dates and times of tardiness.


The output files can be modified by replacing the desired dates of attendace in the code. See line 44 and line 78 . The current code filters date from October onwards.
