import pandas as pd
import psycopg2
import logging
import inspect
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import Common
import json

insert_RPDTable = """ COPY RPDData(RPD_Link,RPD,Updated_Date,Created_Date,Type,Author,Title,Category,Severity,Assignee,Status,Database,Group_Name,Template,Query_Type,Country,Profile,Industry_Type,Question_Type,  
Report_Type,Time_Series,Year,Company_Priority,SDB_STD_Code_Number,Field_Name,Specific_Account_Name,Company_Name,PPI,Memo_definition_as_reference,Comments) 
 FROM '"""
commands = [ 'alter table RPDData add column document tsvector;',
             'update RPDData set document = to_tsvector(title || ' ' || country || ' ' || author);',
              'alter table RPDData add  column document_with_idx tsvector;'
              'update RPDData set document_with_idx = to_tsvector(title || ' ' || country || ' ' || author);' 
              'create index document_idx on RPDData using GIN (document_with_idx)'
             ]
searchQuery_S2 = """ SELECT title,country,profile,
    (title || ' ' || country || ' ' || author) AS document 
FROM RPDData where document_with_idx  @@ to_tsquery('GAT') or 
document_with_idx @@ to_tsquery('Japan') or document_with_idx @@ to_tsquery('Jen & Z.& Yu') """

searchQuery_S1 = """ SELECT title,country,profile,
                    (country) AS document 
                    FROM RPDData where document_with_idx  @@ to_tsquery('Japan & Rise') or 
                    document_with_idx  @@ to_tsquery('Japan') or
                    document_with_idx  @@ to_tsquery('Rise') """

searchQuery = """ SELECT title,country,profile,
                    (country) AS document 
                    FROM RPDData where document_with_idx  @@ to_tsquery('Japan & Rise') or 
                    document_with_idx  @@ to_tsquery('Japan') or
                    document_with_idx  @@ to_tsquery('Rise') """

ExectionTime = """explain analyze SELECT title,country,profile,
                    (country) AS document 
                    FROM RPDData where document_with_idx  @@ to_tsquery('Japan & Rise') or 
                    document_with_idx  @@ to_tsquery('Japan') or
                    document_with_idx  @@ to_tsquery('Rise') """

connection = psycopg2.connect(host="localhost", database="SampleDB", user="postgres", password="Priyash@24")


def load_excel(SourceFile):
    log = Common.common.getlogger("_")
    read_file = pd.read_excel(SourceFile)
    excel_data = pd.DataFrame(read_file)
    return excel_data

def convert_toCSV(excel_data):
    csvfile = excel_data.to_csv(r'InputData.csv', index=None, header=True)
    return csvfile

def convert_toJSON(excel_data):
    jsondata = excel_data.to_dict(orient='records')
    print(jsondata)
    json_object = json.dumps(jsondata, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    return jsondata


def load_intoDBTable(CSV_Filename):
    log = Common.common.getlogger("_")
    with connection:
        with connection.cursor() as cursor:
            copyQuery =  CSV_Filename + """' DELIMITER ',' CSV HEADER; """
            copyQuery = insert_RPDTable + copyQuery
            log.info("Copy Query" + copyQuery)
            cursor.execute(copyQuery)
            log.info("SELECT * from RPDData")
            RPDTable = """  SELECT * from RPDData """
            cursor.execute(RPDTable)
            result = cursor.fetchall();
            colnames = [desc[0] for desc in cursor.description]
            log.info("List of column names of a table" +str(colnames))
            RPDData = pd.DataFrame(result, columns=colnames)
            log.info("Total number of rows and columns in RPD Data" +str(RPDData.shape))

def create_index():
    log = Common.common.getlogger("_")
    log.info("Index has created has started")

    with connection:
        with connection.cursor() as cursor:
            # create table one by one
            for command in commands:
                cursor.execute(command)
            cursor.commit()
    log.info("Index creation has completed")

def search_results():
    log = Common.common.getlogger("_")
    log.info("search result process has started")
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(searchQuery)
            result = cursor.fetchall();
            colnames = [desc[0] for desc in cursor.description]
            log.info("List of column names of a table" + str(colnames))
    RPDData = pd.DataFrame(result, columns=colnames)
    log.info("Total number of rows and columns in  search results" + str(RPDData.shape))
    log.info(RPDData)
    log.info("search result process has  completed")

def execution_time():
    log = Common.common.getlogger("_")
    log.info("Calculating the execution time for the given search results")
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ExectionTime)
            result = cursor.fetchall();
            colnames = [desc[0] for desc in cursor.description]
            log.info("List of column names of a table" + str(colnames))
    exectiontime = pd.DataFrame(result, columns=colnames)
    log.info(exectiontime)
    log.info("Calculating the execution time  has  completed")







