import psycopg2 

connection = psycopg2.connect('dbname=brandon')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')
# How to insert info into a table
cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);' , (3, True))
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(ident)s, %(completed)s);', {'ident': 2, 'completed': False })



# How to fetch the data 

# First we have to call the data from the table
cursor.execute('SELECT * from table2;')

# Then we can use a fetchall command
result = cursor.fetchall()
print(result)

# we can also use fetchmany(3) -- which fetches 3 results
# or fetchone() -- which fetches the first result


# this is to comit the connection
connection.commit()

# Then we must close the connection & the cursos
connection.close()
cursor.close()