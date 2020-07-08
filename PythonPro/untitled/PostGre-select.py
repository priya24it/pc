import psycopg2
import pandas as pd

conn = psycopg2.connect(host="localhost",database="SampleDB", user="postgres", password="Priyash@24")

sql = "select * from  vendors"

vendor_id = '1'
vendor_name = 'updatedbyPython_Code'
cur = conn.cursor()
# execute the UPDATE  statement
cur.execute(sql)
result = cur.fetchall();
colnames = [desc[0] for desc in cur.description]
print(colnames)
result = pd.DataFrame(result,columns=colnames)
print(result)

# get the number of updated rows
#updated_rows = cur.rowcount
#print(updated_rows)
# Commit the changes to the database
conn.commit()
# Close communication with the PostgreSQL database
cur.close()
