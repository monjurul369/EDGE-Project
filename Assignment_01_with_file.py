import json

file_path = "./Patients_data.json"

def load_data():
    with open(file_path, "r") as file:
        return json.load(file)

def save_data():
    with open(file_path, "w") as file:
        json.dump(patients, file, indent=4)

patients = load_data()

def valid_id():
    duplicate_id = False
    while True:
        id = input("\nEnter patient's ID: ")
        for i in range(len(patients)):
            if patients[i]["id"] == id:
                duplicate_id = True
                print("This patient ID already exists.")
        if duplicate_id:
            print("Please enter another ID.")
            duplicate_id = False
        else:
            break
    
    return id


def add_patient():
    id = valid_id()
    name = input("Enter patient's name: ")
    bg = input("Enter patient's blood group: ")
    room = input("Enter patient's room number: ")

    info = {
        "id": id,
        "name": name,
        "bg": bg,
        "room": room
    }

    patients.append(info)
    save_data()
    print("The patient's information added successfully.")


def view():
    print(f"\nTotal Patients = {len(patients)}")
    for i in range(len(patients)):
        print(f"\nPatient no: {i+1}")
        print(f"ID = {patients[i]["id"]}")
        print(f"Name = {patients[i]["name"]}")
        print(f"Blood Group = {patients[i]["bg"]}")
        print(f"Room No = {patients[i]["room"]}")


def search():
    count = 0
    search_value = input("Enter patients ID/Name/Blood Ground/Room No: ").upper()
    for i in range(len(patients)):
        if search_value in [patients[i]["id"].upper(), patients[i]["name"].upper(), patients[i]["bg"].upper(), patients[i]["room"].upper()] or search_value in  (patients[i]["name"].upper().split()):
            print(f"\nID = {patients[i]["id"]}")
            print(f"Name = {patients[i]["name"]}")
            print(f"Blood Group = {patients[i]["bg"]}")
            print(f"Room No = {patients[i]["room"]}")
            count += 1
    
    if count:
        print(f"\nTotal {count} patients matches with your information.")
    else:
        print("\nNo patient found with this informations.")
    
    
def edit():
    edit_id = input("Enter patients ID to edit: ")
    for i in range(len(patients)):
        if edit_id == patients[i]["id"]:
            patients[i]["id"] = ""
            print("\nPlease fill this with edited informations.")
            id = valid_id()
            name = input("Enter patient's name: ")
            bg = input("Enter patient's blood group: ")
            room = input("Enter patient's room number: ")

            patients[i]["id"] = id
            patients[i]["name"] = name
            patients[i]["bg"] = bg
            patients[i]["room"] = room

            save_data()

            print("All informations edited successfully.")
            break
    else:
        print("\nNo patient found with this informations.")


def delete():
    del_id = input("Enter patients ID to delete: ")
    for i in range(len(patients)):
        if del_id == patients[i]["id"]:
            patients.pop(i)
            save_data()
            print("The patient's information deleted successfully.")
            break
    else:
        print("\nNo patient found with this informations.")

while True:
    print("\n")
    print("Welcome to Patient Management System (MIS).")
    print("1. Add New Patient")
    print("2. View All")
    print("3. Search Patient")
    print("4. Edit Patient's Details")
    print("5. Delete Patient")
    print("6. Exit")
    user_choice = int(input("\nPlease enter your choice: "))

    match user_choice:
        case 1:
            add_patient()
        case 2:
            view()
        case 3:
            search()
        case 4:
            edit()
        case 5:
            delete()
        case 6:
            print("Thanks for using our system.")
            break
        case _:
            print("Invalid Input! Try again.")