Udacity Data Engineer Project 1

Purpose :

Build an ETL pipeline for Sparkify to process their song and log data collected from users so that the data could be used for next-step analysis. The data were stored in PostgreSQL, in the database named sparkify. 

This pipeline builds data models with a star schema. with the pipeline, five tables were created in spartify:

    1 fact table: songplays
    4 dimension tables:  users, songs, artist, time
    

What is included in the ETL pipeline: 

data: a folder including song and user activity data.

look_log.ipynb: gives you a peek at the structure of the log data.

sql_queries.py: defines SQL queries to create tables, insert records to table, join tables, and drop table.

create_tables.py: creates tables with column names.

etl.ipynb :  reads data from files and inserts data into tables. (This is a prototype for development. It only processes partial data. To generate a complete dataset, use etl.py)

etl.py: reads data from files and inserts data into tables. 

test.ipynb: checks if the ETL pipeline works successfully.

Data model schema: please see the file "sparkifyDB_star_schema.pdf"
