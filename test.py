import psycopg2 

con = psycopg2.connect(host="localhost", database="magicspaces", user="postgres", password="pgpass")
cur = con.cursor()

# print("----- Inserting values -----")
# cur.execute('INSERT INTO payments ("id", "payDescription", "payDate") VALUES (\'5\', \'5 Payment\', \'2020-02-02\')')
# con.commit()

# print("----- Viewing all values -----")
# cur.execute('SELECT * from public."registration"')
# rows = cur.fetchall()
# for row in rows:
#     print(f'ID is: {row[0]} description is: {row[1]} Date is: {row[2]}')

print("----- Viewing select values -----")

# cur.execute('SELECT "payDescription" from payments where id = 3')
# value = cur.fetchall()
# for a in value:
#     print(a[0])

client = 'ms0001'
#cur.execute("SELECT * FROM payments WHERE id = id", client)
cur.execute("SELECT * FROM payments WHERE clientid = %s", (client,))
value = cur.fetchall()
print (value)




# print("----- Viewing where clause values -----")
# testID = 4
# cur.execute('SELECT "payDescription" from payments where id = id', testID)
# value = cur.fetchall()
# for a in value:
#     print(a[0])

