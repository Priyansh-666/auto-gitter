import tkinter as tk
from tkinter import simpledialog
import os
import subprocess

def create_bat_file(username, web_address, branch):
    # Define the content of the .bat file
    bat_content = f'''
    @echo off
    git init
    git add .
    git commit -m "update"
    git branch {branch}
    git remote add {username} {web_address}
    git push {username} {branch}
    '''

    # Save the content to a .bat file
    with open("add_remote.bat", "w") as bat_file:
        bat_file.write(bat_content)

def get_user_inputs():
    # Ask for username and web address
    username = simpledialog.askstring("Username", "Enter username:")
    web_address = simpledialog.askstring("Web Address", "Enter repository (URL):")

    if username is not None and web_address is not None:
        # Ask for branch
        branch = simpledialog.askstring("Branch", "Enter branch:")
        if branch is not None:
            # Create the .bat file
            create_bat_file(username, web_address, branch)
            print("Bat file created successfully.")
        else:
            print("Branch not provided. Bat file not created.")
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

def py_dock():
    content = f'''
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
'''
    
    with open("dockerfile", "w") as bat_file:
        bat_file.write(content)


def run_command_in_terminal(command, terminal_widget):
    terminal_widget.config(state=tk.NORMAL)  # Enable editing to insert command
    terminal_widget.insert(tk.END, f"$ {command}\n")
    terminal_widget.config(state=tk.DISABLED)  # Disable editing again
    terminal_widget.update_idletasks()

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        terminal_widget.config(state=tk.NORMAL)  # Enable editing to insert output
        terminal_widget.insert(tk.END, result.stdout)
        terminal_widget.insert(tk.END, result.stderr)
        terminal_widget.config(state=tk.DISABLED)  # Disable editing again
    except Exception as e:
        terminal_widget.config(state=tk.NORMAL)  # Enable editing to insert error message
        terminal_widget.insert(tk.END, f"An error occurred: {str(e)}\n")
        terminal_widget.config(state=tk.DISABLED)  # Disable editing again

    terminal_widget.config(state=tk.NORMAL)  # Enable editing to add newline
    terminal_widget.insert(tk.END, "\n")
    terminal_widget.config(state=tk.DISABLED)  # Disable editing again
    terminal_widget.see(tk.END)
    terminal_widget.update_idletasks()

def open_docker_window():
    global filename  # Use the global filename variable
    docker_window = tk.Toplevel()
    docker_window.title("Docker Commands")

    flask_label = tk.Label(docker_window, text="This is only meant for Flask apps", fg="red")
    flask_label.pack(pady=10)


    dockerfile_button = tk.Button(docker_window, text="Create Dockerfile", command=py_dock)
    dockerfile_button.pack(pady=10)

    build_docker_button = tk.Button(docker_window, text="Build Docker Image", command=lambda: run_command_in_terminal(f"docker build -t {filename} .", terminal))
    build_docker_button.pack(pady=10)

    run_docker_button = tk.Button(docker_window, text="Run Docker Container", command=lambda: run_command_in_terminal(f"docker run -p 5000:5000 {filename}", terminal))
    run_docker_button.pack(pady=10)

    filename = simpledialog.askstring("Filename", "Enter filename:")
    if filename:
        filename_label = tk.Label(docker_window, text=f"Filename set to: {filename}")
        filename_label.pack(pady=10)

    # Create a text widget for terminal-like output
    terminal = tk.Text(docker_window, wrap=tk.WORD)
    terminal.pack(fill=tk.BOTH, expand=True)
    terminal.config(state=tk.DISABLED)  # Make the text widget read-only

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

    docker_window_button = tk.Button(root, text="Open Docker Commands Window", command=open_docker_window)
    docker_window_button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    create_buttons()
