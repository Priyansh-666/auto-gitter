import tkinter as tk
from tkinter import simpledialog

def create_bat_file(username, web_address):
    # Define the content of the .bat file
    bat_content = f'''
    git add .
    git commit -m "update"
    git remote add {username} {web_address}
    git push {username} master
    '''

    # Save the content to a .bat file
    with open("add_remote.bat", "w") as bat_file:
        bat_file.write(bat_content)

def get_user_inputs():
    # Ask for username and web address
    username = simpledialog.askstring("Username", "Enter username:")
    web_address = simpledialog.askstring("Web Address", "Enter web address (URL):")

    if username is not None and web_address is not None:
        # Create the .bat file
        create_bat_file(username, web_address)
        print("Bat file created successfully.")
    else:
        print("User inputs not provided. Bat file not created.")

if __name__ == "__main__":
    get_user_inputs()
