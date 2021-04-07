Q1:
LINK: https://livesql.oracle.com/apex/livesql/s/lf1jbqau43onmp6mbjvxtxxee

ASSUMPTIONS:
1. Created only 2 tables, "Appointment" which stores all the information about a particular Appointment.
2. "DentalProcedureCodes" which stores the Procedure-Codes and their price.
3. Subtracted the start_time and End_time of an appointment to find the average procedure length.
4. Assumed: There is only one procedure happening in each appointment. Though, if needed it can be scaled to multiple procedures in one appointment.
5. At the end I "dropped" both the tables as it was asked in the question.

Main Query: select AVG(dp) as Avgerage_Procedure_Cost_In_Jan,AVG(diff_minutes) as Average_Procedure_Length_Minutes_In_Jan from (select DENTALPROCEDURECODES.PRICE as dp,round((cast(end_time as date) - cast(start_time as date))* 24 * 60) as diff_minutes from appointment inner join DENTALPROCEDURECODES on Appointment.DENTALPROCEDURECODE = DENTALPROCEDURECODES.DENTALPROCEDURECODE where appt_date between '01-JAN-21' AND '31-JAN-21')


Q2:
LINK: https://livesql.oracle.com/apex/livesql/s/lf1k1173ysfrbn7hsv7hk3tg2

ASSUMPTIONS:
1. Showed the earnings from all procedures conducted on 6th January.

Main Query: select SUM(DENTALPROCEDURECODES.PRICE) AS Earnings_For_6th_Jan from Appointment inner join DENTALPROCEDURECODES on Appointment.DENTALPROCEDURECODE = DENTALPROCEDURECODES.DENTALPROCEDURECODE where appt_date = '6-JAN-21'


Q3:
LINK: https://livesql.oracle.com/apex/livesql/s/lfsku9umheu2ohrs2ppiznkv4

ASSUMPTIONS:
1. Have displayed the employee_id of all the staff members who can do more than 5 tasks out of which, at least 5 tasks should be:

File taxes
Meet the press
Organize spring cleaning
Do teeth cleaning
Reorder inventory

Q4:
LINK: https://livesql.oracle.com/apex/livesql/s/lf1o53a7lemnw3cxsoizqlhd8

Question: Print the number of procedures each doctor/dentist has performed in the clinic in increasing order of number of procedure performed.

Main Query : select doctor.doctor_name,count(appointment.doctor_id) as Number_Of_Appointments_Taken from Appointment inner join doctor on Appointment.doctor_Id = doctor.employee_id group by doctor.doctor_name order by count(appointment.doctor_id)
