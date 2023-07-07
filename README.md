# Data-Engineer-Interview



Section - 1 - Python ( All Codes Below Given are Python Codes )
-------------------------

#### Have a list of 3 letters. Write a Python code to concatenate this list with another list of numbers whose range varies from 1 to 3 (3 is included).

**Input:** letters list = ['A', 'B', 'C]

**Expected Output:** [A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']



Section - 2 - Spark ( All Codes Below Given are Python Codes )
-------------------------

#### Write a Spark code to standarize the column names in the dataframe. All columns should be smaller case and replace space with underscore().

**employees.csv**

Emp Id, Emp Name, Dept Name <br />
101, Alice, Sales <br />
102, Bob, Sales, <br />


**Expected Output:**

emp_id,emp_name,dept name
101, Alice, Sales
102, Bob, Sales



Section - 3 - Customise a CICD pipeline 
-------------------------

#### Customise the Github Actions pipeline to run some unit tests on the code you have created previously.



Section - 4 - AWS Application High Level Design 
-------------------------
#### Let's say the following, we receive around 100k avro files hourly in raw s3 bucket and we would like to parse these files and dump them into parquet table in curated s3 bucket. Please use DRAW.IO and suggest a solution to achieve this target using aws services and including monitoring and alerting features. 
