import psycopg2

conn = psycopg2.connect(host="localhost",database="SampleDB", user="postgres", password="Priyash@24")

sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""

vendor_id = '1'
vendor_name = 'updatedbyPython_Code'
cur = conn.cursor()
# execute the UPDATE  statement
cur.execute(sql, (vendor_name, vendor_id))
# get the number of updated rows
updated_rows = cur.rowcount
print(updated_rows)
# Commit the changes to the database
conn.commit()
# Close communication with the PostgreSQL database
cur.close()
