import pandas as pd
import psycopg2

read_file = pd.read_excel(r'InputData.xlsx')
excel_data = pd.DataFrame(read_file)
print(excel_data.shape)
print(excel_data.columns.tolist())
listofcolumns  = excel_data.columns.tolist()
read_file.to_csv(r'InputData.csv', index = None, header=True)
#option_values = [(option_text, 'character varying(255)') for option_text in listofcolumns]
#print(option_values)
csvfile = r"C:\Python Pro\untitled\InputData.csv"
command = """ COPY RPDData(RPD_Link,RPD,Updated_Date,Created_Date,Type,Author,Title,Category,Severity,Assignee,Status,Database,Group_Name,Template,Query_Type,Country,Profile,Industry_Type,Question_Type,  
Report_Type,Time_Series,Year,Company_Priority,SDB_STD_Code_Number,Field_Name,Specific_Account_Name,Company_Name,PPI,Memo_definition_as_reference,Comments) 
FROM '""" + csvfile+ """' DELIMITER ',' CSV HEADER; """
print(command)
conn = psycopg2.connect(host="localhost",database="SampleDB", user="postgres", password="Priyash@24")
cur = conn.cursor()
cur.execute(command)
conn.commit()
finalresult = """  SELECT title,country,profile,
    (title || ' ' || country || ' ' || author) AS document 
FROM RPDData where document_with_idx  @@ to_tsquery('GAT') or 
document_with_idx @@ to_tsquery('Japan') or document_with_idx @@ to_tsquery('Jen & Z.& Yu')   """
cur.execute(finalresult)
result = cur.fetchall();
colnames = [desc[0] for desc in cur.description]
print(colnames)
result = pd.DataFrame(result,columns=colnames)
print(result)

