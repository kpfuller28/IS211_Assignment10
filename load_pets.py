import sqlite3


def main():
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS person")
    cursor.execute("DROP TABLE IF EXISTS pet")
    cursor.execute("DROP TABLE IF EXISTS person_pet")
    cursor.execute(
        "CREATE TABLE person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER);"
    )
    cursor.execute(
        "CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER);"
    )
    cursor.execute("CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGE);")

    # The purpose fo the person_pet table is to define a many-to-many relationship between the person table and the pets table. This makes it so each person can have multiple pets, and each pet can possibly have multiple owners.

    cursor.execute("INSERT INTO person VALUES (1,'James','Smith',41)")
    cursor.execute("INSERT INTO person VALUES (2,'Diana','Greene',23)")
    cursor.execute("INSERT INTO person VALUES (3, 'Sara','White',27)")
    cursor.execute("INSERT INTO person VALUES (4,'William','Gibson',23)")
    cursor.execute("INSERT INTO pet VALUES (1,'Rusty','Dalmation',4,1)")
    cursor.execute("INSERT INTO pet VALUES (2,'Bella','Alaskan Malamute',3,0)")
    cursor.execute("INSERT INTO pet VALUES (3,'Max','Cocker Spaniel',1,0)")
    cursor.execute("INSERT INTO pet VALUES (4,'Rocky','Beagle',7,0)")
    cursor.execute("INSERT INTO pet VALUES (5,'Rufus','Cocker Spaniel',1,0)")
    cursor.execute("INSERT INTO pet VALUES (6,'Spot','Bloodhound',2,1)")
    cursor.execute("INSERT INTO person_pet VALUES (1,1)")
    cursor.execute("INSERT INTO person_pet VALUES (1,2)")
    cursor.execute("INSERT INTO person_pet VALUES (2,3)")
    cursor.execute("INSERT INTO person_pet VALUES (2,4)")
    cursor.execute("INSERT INTO person_pet VALUES (3,5)")
    cursor.execute("INSERT INTO person_pet VALUES (4,6)")
    connection.commit()
    connection.close()


if __name__ == "__main__":
    print("Running load_pets.py")


main()
