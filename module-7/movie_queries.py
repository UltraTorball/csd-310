import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "***************",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno ==  errorcode.ER_BAD_DB_ERROR:
        print("  THe specified database does not exist")

    else:
        print(err)

cursor = db.cursor()
print("-- DISPLAYING Studio RECORDS --\n")
cursor.execute("SELECT studio_id, studio_name FROM studio")

studios = cursor.fetchall()

for studio in studios:

    print("Studio ID: {}\n Studio Name: {}\n".format(studio[0],studio[1]))
print("-- DISPLAYING Genre RECORDS --\n")
cursor.execute("SELECT genre_id, genre_name FROM genre")

genres = cursor.fetchall()
for genre in genres:

    print("Genre ID: {}\n Genre Name: {}\n".format(genre[0],genre[1]))

print("-- DISPLAYING Short Film RECORDS --\n")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

films = cursor.fetchall()
for film in films:

        print("Film Name: {}\n Runtime: {}\n".format(film[0], film[1]))

print("-- DISPLAYING Director RECORDS in Order --\n")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

films = cursor.fetchall()
for film in films:

        print("Film Name: {}\n Director: {}\n".format(film[0], film[1]))
