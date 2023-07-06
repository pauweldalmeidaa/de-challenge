# Data-Engineer-Interview


### Section - 1 - Python ( All Codes Below Given are Python Codes )

#### The marks of a student in each subject given below. Write a Python function that takes two parameters 'name' and 'subjects_marks. Finally, print the student's name and all the subjects in which his/her marks are above 60. If the 'name' is not provided, print 'None.'

**Input:** Maths = 80, Physics = 58, Chemistry = 62, English = 72, Biology = 50

**Expected Output:** Name: Vishnu - Subjects: {'Chemistry', 'English', 'Mathematics"}




### Section - 2 - Spark ( All Codes Below Given are Python Codes )

#### Let's say the following describes the contents of Sync.txt, Use PySpark to read the contents of a text file named "sync.txt" to get the required result.

**sync.txt**

1,Rahul,Dravid-10000 <br />
2,Virat,Kohli-20000 <br />
3,MS,Dhoni,27000 <br />
4,Dinesh,Karthik,18000 <br />


**Desired Output**

| ID|First Name  |Last Name  |Salary |
|---|:----------:|:---------:|------:|
|  1|     Rahul  |   Dravid  |   10k |
|  2|     Virat  |    Kohli  |   20k |
|  3|        MS  |    Dhoni  |   27k |
|  4|    Dinesh  |   Karthik |   18k |



### Section - 3 - AWS Application High Level Design 

#### Q1. Let's say the following, we receive around 10k xml files hourly in raw s3 bucket and we would like to parse and unnest these files and dump them into parquet table in trusted s3 bucket. Please use DRAW.IO and suggeste a solution to achieve this target using aws services and including monitoring and alerting features. 
#### Q2. Describe a CICD pipeline to automate the artifacts continuous deployments, independently of the technology.
