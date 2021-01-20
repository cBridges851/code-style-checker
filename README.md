# code-style-checker
This is my final project for the introductory programming and problem solving module at university.

## What This Repository Contains

### Design
- Code Style Checker ERD.png - a series of entity relationship diagrams that have helped to define the structure of the program at various stages of development.
- Code Style Checker Interface.png - the original interface design for the application, which of course is subject to change.

### Program
- program.py - the starter program. Run this file when using the program.
#### FileHandling
- file_logic.py - manages the file handling in the project, such as opening files to be checked.
- \_\_init__.py - treats the project as a package, so classes can be imported despite the file structure.
#### Validators
All the validators that the program uses. These include:  
- \_\_pycache__ - contains Python 3 code that has been compiled and is ready to be executed.
- conditional_statement_signature_quantity_on_line_validator - makes sure there is no more than one conditional statement signature per line.
- end_of_signature_space_validator.py - checks to see if there is a space between the closing curved bracket or word and opening curly bracket in a signature.
- equals_space_missing_validator.py - checks to see if there are any missing spaces before or after an equals sign.
- number_of_classes_validator.py - checks how many classes there are in a JavaScript file. There should be a maximum of 1.
- start_of_signature_space_validator.py - checks to see if there is a space after a loop or conditional statement keyword in the signature.
- validator_runner.py - runs the validators in this folder.
- var_use_validator.py - checks to see if there are any occurrences of `var` in the code. `let` or `const` should be used instead.
- \_\_init__.py - treats the project as a package, so classes can be imported despite the file structure.
#### View
- code_box_manager.py - responsible for edits to the box where the code is inputted. This includes displaying the code that is in a file, and inserting and removing the placeholder text.
- comment_remover.py - removes the comments that are in the code so they are not included in the validation.
- favicon.ico - the icon that is in the window.
- interface_renderer.py - renders the user interface so it is displayed when the program is run.
- outputter.py - responsible for outputting the results of the validators.
- \_\_init__.py - treats the project as a package, so classes can be imported despite the file structure.

### Python.gitignore
The files for Git to ignore when pushing to the remote repository.

### README.md
What you are reading right now! This aims to give you all the information you need to know about this project.

## Python Features Used
- Variables  
- Inputs and Outputs  
- Conditional Statements  
- Lists  
- Dictionaries  
- Loops  
- Tkinter  
- Object-Oriented Programming
