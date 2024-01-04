import json
import pyinputplus as pyin

DATA = []


def create_data():
    file_path = "data.json"
    try:
        with open(file_path, 'r') as json_file:
            loaded_list = json.load(json_file)
            DATA.extend(loaded_list)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print(f"File not found or JSON decode error. Creating a new file.")


def ask_inputs():
    global DATA
    num_persons = int(input("Enter the number of persons: "))

    for _ in range(num_persons):
        user_date = pyin.inputDate(prompt="Please enter the date using format d-m-y: ", formats=["%d-%m-%Y"])
        user_date_str = user_date.strftime("%d-%m-%Y")
        user_name = input("Please enter your name: ")
        user_food = pyin.inputInt(prompt="Please enter the $ amount you spent on food this month: ")
        user_bills = pyin.inputInt(prompt="Please enter the $ amount you spent on bills this month: ")
        user_mortgage = pyin.inputInt(prompt="Please enter the $ amount you spent on mortgage this month: ")
        user_savings = pyin.inputInt(prompt="Please enter the $ amount you added as savings this month: ")

        person_data = {
            "Date": user_date_str,
            "Person": user_name,
            "Food": user_food,
            "Bills": user_bills,
            "Mortgage": user_mortgage,
            "Savings": user_savings,
            "Total": user_food + user_bills + user_mortgage
        }

        existing_person_index = next((idx for idx, person in enumerate(DATA) if person["Person"] == user_name), None)

        if existing_person_index is not None:
            update_choice = pyin.inputYesNo(prompt=f"Person {user_name} already exists. Do you want to update? (yes/no): ")
            if update_choice.lower() == "yes":
                DATA[existing_person_index] = person_data
        else:
            DATA.append(person_data)

    return DATA


def delete_person():
    global DATA
    delete_choice = input("If you want to delete a person, enter the person's name (or leave blank): ")
    if delete_choice:
        DATA = [person for person in DATA if person["Person"] != delete_choice]

    return DATA


def save_data():
    global DATA
    file_path = "data.json"
    with open(file_path, 'w') as json_file:
        json.dump(DATA, json_file, indent=4)


def print_data():
    global DATA
    for idx, person_data in enumerate(DATA, start=1):
        print(
            f"\nData for Person {idx}:"
            f"\n{person_data['Person']}, at the date {person_data['Date']}, you spent in total {person_data['Total']}$ and saved {person_data['Savings']}$."
        )


create_data()
ask_inputs()
delete_person()
save_data()
print_data()

