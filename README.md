Purpose :

Build an ETL pipeline for Sparkify to process their song and log data collected from users, so the data could be used for next step analysis. The data were stored in postgreSQL, in the database named sparkify. 

This pipeline build data models with star schema. with the pipeline, 5 tables were created in spartify:

    1 Fact Table : songplays
    4 Dimension Tables:  users, songs, artist, time
    

What is inuded in the ETL pipeline: 

data: a folder including song and user activity data.

look_log.ipynb:gives you a peek on the structure of the log data.

sql_queries.py: defines sql queries to create table, insert records to table, join tables, and drop table.

create_tables.py : creates tables with column names.

etl.ipynb :  reads data from files and inserts data in to tables. (This is a prototype for development, it only process partial data. To generate a full dataset, use etl.py)

etl.py : reads data from files and inserts data into tables. 

test.ipynb: checks if the ETL pipline works sucessfully.

Data model schema

<img src="sparkify_star_schema.png" hight=500 weight=500 />
