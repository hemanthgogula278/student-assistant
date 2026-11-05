import json
import os

FILE_NAME = "student_data.json"


# Load saved data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {
        "tasks": [],
        "notes": [],
        "timetable": []
    }


# Save data
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


data = load_data()


# Add a task
def add_task():
    task = input("Enter your study task: ")

    data["tasks"].append({
        "task": task,
        "completed": False
    })

    save_data()
    print("Task added successfully!")


# View tasks
def view_tasks():
    print("\n--- YOUR STUDY TASKS ---")

    if not data["tasks"]:
        print("No tasks available.")
        return

    for i, task in enumerate(data["tasks"], 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")


# Complete a task
def complete_task():
    view_tasks()

    if not data["tasks"]:
        return

    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(data["tasks"]):
            data["tasks"][number - 1]["completed"] = True
            save_data()
            print("Task completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Add notes
def add_note():
    note = input("Enter your study note: ")

    data["notes"].append(note)
    save_data()

    print("Note saved successfully!")


# View notes
def view_notes():
    print("\n--- YOUR STUDY NOTES ---")

    if not data["notes"]:
        print("No notes available.")
        return

    for i, note in enumerate(data["notes"], 1):
        print(f"{i}. {note}")


# Add timetable
def add_timetable():
    subject = input("Enter subject name: ")
    time = input("Enter study time: ")

    data["timetable"].append({
        "subject": subject,
        "time": time
    })

    save_data()
    print("Timetable added successfully!")


# View timetable
def view_timetable():
    print("\n--- STUDY TIMETABLE ---")

    if not data["timetable"]:
        print("No timetable available.")
        return

    for item in data["timetable"]:
        print(item["time"], "-", item["subject"])


# Main menu
def student_assistant():

    while True:
        print("\n==============================")
        print("     STUDENT ASSISTANT")
        print("==============================")

        print("1. Add Study Task")
        print("2. View Study Tasks")
        print("3. Complete Task")
        print("4. Add Study Notes")
        print("5. View Study Notes")
        print("6. Add Timetable")
        print("7. View Timetable")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            add_note()

        elif choice == "5":
            view_notes()

        elif choice == "6":
            add_timetable()

        elif choice == "7":
            view_timetable()

        elif choice == "8":
            print("Thank you for using Student Assistant!")
            break

        else:
            print("Invalid choice. Try again.")


student_assistant()