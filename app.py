from database import add_entry, view_entries

menu = """Please select one of the following of the follwoing options:
1) New entry
2) View Entries
3) Exit

Your selection: """

welcome = "Welcome to programming progress diary!"

user_input = input(menu)
while user_input != 3:
    if user_input == "1":
        entry_content = input("What did you learn today?")
        entry_date = input("Enter date: ")
        add_entry(entry_content, entry_date)
    elif user_input == "2":
        entries = view_entries()
        for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")
    else:
        print("Please enter either 1, 2, or 3")
    
    user_input = input(menu)