import tkinter as tk
from tkinter import simpledialog
import os

def create_bat_file(username, web_address):
    # Define the content of the .bat file
    bat_content = f'''
    git init
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
    web_address = simpledialog.askstring("Web Address", "Enter repository (URL):")

    if username is not None and web_address is not None:
        # Create the .bat file
        create_bat_file(username, web_address)
        print("Bat file created successfully.")
    else:
        print("User inputs not provided. Bat file not created.")

def create_file_button_clicked():
    get_user_inputs()
def python_ci():
    bat_content = f'''
name: CI/CD

# Controls when the workflow will run
on:
  # Activates the workflow; then there is a push to the main or master branch
  push:
    branches: [main, master]

  # allows you to manually execute this pipeline from the Actions tab.
  workflow_dispatch:
jobs:
    # This workflow contains a single job called "build"
    build:
        # The type of runner that the job will run on
        runs-on: ubuntu-latest
    
        #
        steps:
        - uses: actions/checkout@v2  
        - uses: actions/setup-python@v2  
        - run:  pip install -r requirements.txt  # install requirements to enable GitHub run tests
    '''

    # Save the content to a .bat file
    workflows_dir = ".github/workflows"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(workflows_dir):
        os.makedirs(workflows_dir)
    with open(".github/workflows/pyt.yml", "w") as bat_file:
        bat_file.write(bat_content)
def react_ci():
    bat_content = f'''
#triggers

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

#functions

jobs:

  # build job

    build:

      # Name

      name: Build 

      # The OS to run the job on

      runs-on: ubuntu-latest

      # Steps
      steps:
        - name: Checkout  code 

          uses: actions/checkout@v2

        - name: Install node 16

          uses: actions/setup-node@v1

          with:
            node-version: 16.x

        - name: Install NPM Dependencies
          
          run: npm i 

        - name: Build Project
          run: npm run build
    '''

    # Save the content to a .bat file
    workflows_dir = ".github/workflows"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(workflows_dir):
        os.makedirs(workflows_dir)
    with open(".github/workflows/react_pages.yml", "w") as bat_file:
        bat_file.write(bat_content)

def create_buttons():
    # Create the main window
    root = tk.Tk()
    root.title("Git Automation")

    # Create buttons
    button1 = tk.Button(root, text="Make git auto commiter", command=create_file_button_clicked)
    button1.pack(pady=10)  # Add vertical spacing after the button

    button_python = tk.Button(root, text="Create Python CI/CD", command=python_ci)
    button_python.pack(pady=10)  # Add vertical spacing after the button

    button_react = tk.Button(root, text="Create React CI/CD", command=react_ci)
    button_react.pack(pady=10)  # Add vertical spacing after the button

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    create_buttons()
