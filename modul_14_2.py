import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection. cursor()

cursor. execute ('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
for i in range(1,11):
    cursor. execute( 'INSERT INTO Users (id,username, email, age,balance) VALUES (?,?,?,?,?)',(f"{i}",f"User{i}",
                                                                                f"example{i}@gmail.com", i*10,1000))

    if i%2!=0:
        cursor. execute('UPDATE Users SET balance =? WHERE username =?',
        (500,f"User{i}"))
    if (i-1)%3==0:
        cursor.execute ('DELETE FROM Users WHERE username=?', (f"User{i}",))


        cursor.execute ('DELETE FROM Users WHERE id=?', (6,))
cursor. execute("SELECT COUNT (*) FROM Users ")
total_users=cursor.fetchone()[0]
cursor. execute("SELECT SUM(balance) FROM Users ")
all_balances=cursor.fetchone()[0]
print(all_balances / total_users)


connection. commit()
connection. close()