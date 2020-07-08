import psycopg2

#creating poll means -- which programming language are you learning (Java,Python) , Uusername: Priya,Ashok
#Poll ID: 1 , Title : Java , username:Priya , A user can add multiple options.
from psycopg2.extras import execute_values

CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls
(id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"""
CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER);"""
CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes
(username TEXT, option_id INTEGER);"""

INSERT_POLL = "INSERT INTO polls (title, owner_username) VALUES (%s,%s) RETURNING id;"
INSERT_OPTION = "INSERT INTO options (option_text, poll_id) VALUES (%s,%s);"
INSERT_VOTE = "INSERT INTO votes (username, option_id) VALUES (%s,%s);"


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)
            print("All the tables has craeted succesfully..")

def create_polls(connection):
    with connection:
        with connection.cursor() as cursor:
            options = []
            print("create_polls procedure..")
            text = str(input('Enter the Text'))
            owner = str(input('Owner'))
            i = 0
            while (new_option := input('Enter the option')):
                options.insert(i,new_option)
            print("list of options")
            print(len(options))
            for opt in range(0,len(options)):
                print(options[opt])
            print(INSERT_POLL)
            cursor.execute(INSERT_POLL,(text,owner))
            print('inset statement executed success')
            poll_id = cursor.fetchone()[0]
            option_values = [(option_text, poll_id) for option_text in options]
            print(INSERT_OPTION)
            print(option_values)
           # execute_values(cursor, INSERT_OPTION, option_values)
            cursor.executemany(INSERT_OPTION, option_values)



def voteon_poll(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("select text from polls")
            #cursor.execute(INSERT_VOTE, (username, option_id))



options = """ 1. create new poll
2.List open polls
3.Vote on a poll
4.Show poll votes
5.select a random winner from a poll option
6.Exit """


menuoptions = {
    "1":create_tables,
    "2":create_polls,
    "4":voteon_poll
}

#databaseURL = " host='localhost',database='SampleDB', user='postgres', password='Priyash@24' "
databaseURL = ' host="localhost",database="SampleDB", user="postgres", password="Priyash@24" '
conn = psycopg2.connect(host="localhost",database="SampleDB", user="postgres", password="Priyash@24")

print(options)
n1 =  str(input("Enter your choice"))
print(n1)
#print(menuoptions[n1])

if  n1 <= "7":
    try:
        print("entering the loop.. ")
        print(menuoptions[n1])
        menuoptions[n1](conn)
    except Exception as e:
        print("Exception has entered..")
        print(e)
else:
    print("Invalid number has entered")













