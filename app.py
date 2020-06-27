from database import add_entry, get_entries, createTable

menu = """Please select one of the following of the follwoing options:
1) New entry
2) View Entries
3) Exit

Your selection: """

welcome = "Welcome to programming progress diary!"

def prompt_new_entry():
    entry_content = input("What did you learn today?")
    entry_date = input("Enter date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['entry_date']}\n{entry['entry_content']}\n\n")


print(welcome)
createTable()

user_input = input(menu)
while user_input != 3:
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    elif user_input == "3":
        break
    else:
        print("Please enter either 1, 2, or 3")

    user_input = input(menu)
