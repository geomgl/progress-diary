menu = """Please select one of the following of the follwoing options:
1) New entry
2) View Entries
3) Exit

Your selection """

welcome = "Welcome to programming progress diary!"

user_input = input(menu)
while user_input != 3:
    if user_input == 1:
        print("Adding...")
    elif user_input == 2:
        print("Viewing...")
    else:
        print("Please enter either 1, 2, or 3")
    
    user_input = input(menu)