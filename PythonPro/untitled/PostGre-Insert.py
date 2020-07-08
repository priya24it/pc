import psycopg2

conn = psycopg2.connect(host="localhost",database="SampleDB", user="postgres", password="Priyash@24")

sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"


vendor_list = [
        ('AKM Semiconductor Inc.',),
        ("dr reddy's laboratories",),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]


try:
    cur = conn.cursor()
    # execute the INSERT statement
    cur.executemany(sql, vendor_list)
    # commit the changes to the database
    conn.commit()
    # close communication with the database
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

