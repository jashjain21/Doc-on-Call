# Doc-on-Call
A D.B.M.S project which recommends doctors to patients(new as well as existing ones).

PROJECT REPORT

TOPIC : DOC FOR ALL

Medical/health is the location of the website to be launched

Aim : We aim at catering the needs of patients and providing them with the best of healthcare facilities.We have a doctor recommendation system wherein a patient can track his past appointments and a new patient would be recommended the best doctor available based on their speciality by taking in data about which type of patients a doctor treats the best and also your illness is taken in considerations

## ER Diagram
![](../master/Screenshots/image2.png?raw=true)

## Schema Diagram
![](../master/Screenshots/image24.png?raw=true)

Features
1. Hospital authentication.(register / login)
2. Hospital Personal Information can be viewed
3. Associated Doctors with the hospital can be seen.
4. Doctor authentication.(register / login)
5. Doctor Personal Information can be viewed
6. Patient’s associated with the doctor can be seen.
7. The records and appointments had with the patients can also be viewed by the     
    doctor.
8. Patient authentication.(register / login)
9. Patient Personal Information can be viewed
10.Patient can see his past records create a new record with any doctor
11.Patient can create appointments with the doctors with which they have a record.
12.Patient can rate a doctor after his/her appointment.
13.Any user can see the doctors according to the ratings given to them which are also sorted according to their profession.

TECHNOLOGY USED :
Database: DB Sqlite
Code: Python
Front End: HTML, CSS, Javascript, Bootstrap
Back End: Django


## Home Page
![](../master/Screenshots/image15.png?raw=true)

## Hospital (Signup and Login)
![](../master/Screenshots/image26.png?raw=true)

## Hospital Page (Massaccheutes) :
![](../master/Screenshots/image25.png?raw=true)

## Doctor
![](../master/Screenshots/image20.png?raw=true)

## Doctor (Dorie):
![](../master/Screenshots/image16.png?raw=true)

## Patient
![](../master/Screenshots/image12.png?raw=true)

## Patient Page (Ernesto):
![](../master/Screenshots/image13.png?raw=true)

## Patient Record (New) :
![](../master/Screenshots/image4.png?raw=true)

## Patient Appointment (New):
![](../master/Screenshots/image29.png?raw=true)

## See Doctors:
![](../master/Screenshots/image21.png?raw=true)

## About Us:
![](../master/Screenshots/image31.png?raw=true)

## Contact Us:
![](../master/Screenshots/image22.png?raw=true)

## Admin:
![](../master/Screenshots/image9.png?raw=true)

## Urls.py:
![](../master/Screenshots/image23.png?raw=true)

## Views.py:
![](../master/Screenshots/image14.png?raw=true)

# Models.py:
## Hospital Model
![](../master/Screenshots/image27.png?raw=true)

## Doctor Model
![](../master/Screenshots/image30.png?raw=true)

## Patient Model:
![](../master/Screenshots/image19.png?raw=true)

## Future Scope:
We plan on taking it a step forward by making it an interactive platform which fulfills the needs of doctors as well as patients to the fullest.
When an appointment would be created a patient would be displayed a graph wherein he can view the timings and the dates on which the doctor(specific) would be free and the request made by the patient would be given to the doctor.
Also after the doctor accepts the invitation a meeting would be held between the two and then the doctor would prescribe the medication and the fees and the patient on handing in the fees would rate the doctor.
For anonymity purposes the name of the patient giving the rating wouldn’t be visible.
Also taking it a step forward we would apply machine learning techniques and implement neural networks to understand patient segments and thereby recommending him doctors which he would need at that moment thereby increasing traffic on our site.

## Conclusion:
We were successful in our mission to create a community and cater their needs and demands at the  earliest by recommending them the best quality doctors available so that trust in a relation between us and the patients could be successfully established.
We were successful in harnessing the power of Django which gave us the admin utility which provides  a much better UI than the traditional command line shell for viewing and editing our databases.Moreover our concepts of joints and order by were further enriched.
