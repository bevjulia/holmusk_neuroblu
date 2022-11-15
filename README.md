# Overview
This repository contains source code for Holmusk's technical test. Aside from this README document, you can find additional explanations and details in the `documents.pdf` file. 

## Folder structure
`root`: Contains the task description in PDF, documentation files, python requirements.txt and test_querypackage.py that is used to test the package created for task 2.\
`./synthea`: Folder that contains the generated synthea CSV files, .properties file and JAR file.\
`./synthea_etl`: SQL queries, query plan results and an R script to perform ETL for task 1.\
`./query_package`: Contains the python modules created for task 2.

## Prerequisites
Java version: `11.0.17`\
Python version: `Python 3.8.13`\
R version: `4.2.2`\
PostgreSQL version: `15.1`

# User Guide

Clone this repository into your local development environment. 

For the below tasks, in order for the code to read the database user and password, a `config.env` file needs to be created manually with the following format:
```
DBNAME='neuroblu'
DBUSER='user1'
PASSWORD='user1password'
HOST='localhost'
PORT=5432
```

## Task 1: Generate synthetic EHR data with Synthea

**Step 1**: Follow references in task description to download and set up the Synthea JAR file. Upload the `synthea-with-dependencies.jar` file to the `./synthea` folder

**Step 2**: Run the following commands to generate synthetic EHR data only from Massachusetts. Results are written into the `./synthea/output` folder.
```
cd ./synthea
java -jar synthea-with-dependencies.jar Massachusetts -c ./synthea.properties
```
**Step 3**: Set up a relational database using PostgreSQL. See `documentation.pdf` in the `root` folder for more details.

**Step 4**: Run the following commands to perform ETL and load the generated CSV files into the PostgreSQL database. 
```
cd ./synthea_etl
R synthea_etl.R
```

**Step 5**: Query loaded data. See `documentation.pdf` in the `root` folder for more details on the analysis. The original and optimized SQL queries are located in `./synthea_etl/sql` folder.

## Task 2: Python Package to query synthetic EHR dataset

Step 1: Set up virtual environment
```
cd ./holmusk_neuroblu
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```
Step 2: Run the following command to test the created package. The functions module is defined in `./querypackage/functions.py`. See `documentation.pdf` in the `root` folder for the results.
```
python test_querypackage.py
```

# Challenges and learnings
* While creating the tables based on CDM v5.4 into the PostgreSQL database, some of the tables in the schemas had missing columns compared to the generated CSV files. This resulted in the ETL script throwing an error for missing columns. 
    * Solution:
    Since there were only 2-3 missing columns from some tables, it did not take much time to manually create the columns to match the CSV data. After which, the ETL R script ran as per normal. 
* Currently learning to use Git Actions for continuous integration. 




