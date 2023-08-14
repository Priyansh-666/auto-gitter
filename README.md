# auto-gitter
Automatically push to git repository by initiating your credentials once.

# Usage for git auto-commiter
You need to have ```git``` installed on your system.

Copy ```auto-commiter``` application in the current working directory of any program/software that you are making.

Run ```auto-commiter``` and enter you github username and then the repository that you want to push in.

A new bat file named ```add_remote``` will be created.

Then just run the ```add_remote``` file and Voila! your files will be uploaded on your repository.

You dont need to run ```auto-commiter``` again and again , its just one time initiation.

Run again if you think you entered wrong Username Or Repository name.

# Usage to create CI/CD for python or react

Copy ```auto-commiter``` application in the current working directory of any program/software that you are making.

Run ```auto-commiter``` and click on ```python CI/CD``` or ```React CI/CD``` based on what you are using.

The ```.yml``` will be created in ```.github/workflows``` and will be ready to be run.

You can change ```.yml``` file as per your deployment host.

# Warning

DONT FORGET TO SIGNUP ON GITHUB FROM YOUR COMPUTER

Go to ```Command Prompt```

Run ```git config --global user.name "FIRST_NAME LAST_NAME"```

Then run ```git config --global user.email "YOUR EMAIL ADDRESS YOU LOGGED IN GITHUB"```
