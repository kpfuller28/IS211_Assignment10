import sqlite3


def query(id):
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()

    personData = cursor.execute(
        "SELECT * FROM person WHERE id = ?",
        (id,),
    ).fetchone()
    if personData is None:
        print(f"Error finding person with ID {id}. Please try again.")
        return

    petData = cursor.execute(
        "SELECT * FROM pet INNER JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id = ?",
        (id,),
    ).fetchall()
    if petData is None:
        print(f"Error acquiring pet data for person with ID {id}")
        return

    name = f"{personData[1]} {personData[2]}"
    age = personData[3]

    print(f"{name}, {age} years old")
    for pet in petData:
        petName = pet[1]
        petBreed = pet[2]
        petAge = pet[3]

        if pet[4] == 1:
            tenses = ("owned", "was")
        else:
            tenses = ("owns", "is")
        print(
            f"{name} {tenses[0]} {petName}, a {petBreed.lower()}, that {tenses[1]} {petAge} years old."
        )


def main():

    while True:
        userInput = input(
            "Please input the ID of the person you would like to look up (input -1 at any time to quit): "
        )
        try:
            personID = int(userInput)
            if personID == -1:
                break
            else:
                print("querying...")
                query(personID)
        except:
            print(
                f"Invalid input. Please input an integer for the ID of the person you want to look up (input -1 at any time to quit)"
            )


if __name__ == "__main__":
    print("Running query_pets.py")

main()
