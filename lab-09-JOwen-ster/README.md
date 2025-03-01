[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/NshmRtUp)
# Laboratory 9

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using standard modules.

## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```

1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/CSUF-CPSC223P-NILAYJAIN12/Lab-09.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd lab09-username
     ```
     
## Program Instructions

Python Standard Modules Usage: In this lab, you will explore the usage of various Python standard modules. Please complete the following tasks:

**[You are provided with main.py file inside which you need to make the changes as per the below tasks]**

**Task 1: Operating System (os)**

Write a Python program that uses the os module to list all files in a specific directory and display their names.

**Task 2: Regular Expressions (re)**

Write a Python program that uses the re module to search for and extract email addresses from a given text.

**Task 3: Mathematics (math)**

Write a Python program that calculates the square root of a user-inputted number using the math module.

**Task 4: Random Numbers (random)**

Write a Python program that generates and prints a random integer between a specified range using the random module.

**Task 5: Statistics (statistics)**

Write a Python program that computes the mean and standard deviation of a list of numbers using the statistics module.

**Task 6: Date and Time (datetime)**

Write a Python program that prints the current date and time using the datetime module.

**Task 7: Performance Timing (timeit)**

Write a Python program that measures the time it takes to execute a simple function using the timeit module.

**Task 8: Reprlib (reprlib)**

Write a Python program that demonstrates the use of reprlib to create a concise representation of a long string.

**Task 9: Pretty Printing (pprint)**

Write a Python program that uses the pprint module to pretty-print a nested dictionary.

**Task 10: Text Wrapping (textwrap)**

Write a Python program that uses the textwrap module to format a long text paragraph into multiple lines with a specified line width.

**Task 11: Template Strings (string.Template)**

Write a Python program that uses the string.Template class to generate dynamic SQL queries with placeholders.

**Task 12: Logging (logging)**

Write a Python program that sets up logging to record events to a log file using the logging module.

**Task 13: Heap Queue (heapq)**

Write a Python program that uses the heapq module to perform heap operations on a list of integers.

**EXPECTED OUTPUT [OUTPUT VALUES COULD BE DIFFERENT HOWEVER OUTPUT FORMAT SHOULD BE SAME AS BELOW]:**
```
.\app.log
.\sample.py
.\LabFolder\data.txt   
.\LabFolder\lab_log.txt
.\__pycache__\bank_exceptions.cpython-311.pyc
.\__pycache__\first_module.cpython-311.pyc
.\__pycache__\mymodule.cpython-311.pyc
.\__pycache__\sample.cpython-311.pyc
.\__pycache__\second_module.cpython-311.pyc
.\__pycache__\test.cpython-311.pyc
abc@example.com
xyz@domain.com
Square root of 16 is 4.0
Random integer between 1 and 100: 92
Mean: 6, Standard Deviation: 3.1622776601683795
Current Date and Time: 2023-11-08 00:06:33.345713
Time taken to execute the function 10000 times: 0.0011316000018268824 seconds
Truncated String: 'This is a ve...be truncated.'
{'age': 30,
 'city': 'New York',
 'name': 'John'}
This is a long paragraph that
needs to be wrapped to
multiple lines for better
readability.
Generated SQL Query: SELECT id, name, email FROM users
Heapified List: [1, 1, 4, 3, 5, 9]
Smallest Element: 1
```

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
main.py
output_screenshot
```
    
## Grading
All points add up to a total of 100 points possible, as detailed below. Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|30|main.py file submitted contains the main driver program and meets the program requirements|
|20|If the output is similar to the expected output given in the readme.md file|

**NOTE: OUTPUT CAN BE DIFFERENT, BUT FORMAT SHOULD BE SIMILAR!**
