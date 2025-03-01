[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/gqw-SMqK)
# Laboratory 8

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using:
     1. classes
     2. inheritance
1. Run and test a Python program.

## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```

1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/CSUF-CPSC223P-NILAYJAIN12/Lab-08.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd lab08-username
     ```
     
## Program Instructions

You are required to create a Python program that demonstrates your understanding of the following concepts: Classes and Objects, Class variables and Instance variables, Inheritance, Multiple Inheritance, Private and Protected variables, and Generators in Python.

**NOTE: You are provided with a file 'main.py' where you have to write your code. Do not modify the provided driver code.**

**Task 1: Classes and Objects**

1. Create a class named **Vehicle** with the following attributes:
- make (a string representing the vehicle's make)
- model (a string representing the vehicle's model)
- year (an integer representing the manufacturing year)

**Task 2: Class Variables and Instance Variables**
1. Add a class variable **vehicle_count** and initialize to 0 to the Vehicle class to keep track of the total number of vehicle instances created.
2. Create a method named **display_vehicle_count()** in the Vehicle class to display the vehicle_count.

**Task 3: Inheritance**
1. Create a subclass named **Car** that inherits from the **Vehicle** class.
2. Add a new attribute **fuel_type** to the Car class (e.g., "Gasoline", "Electric", etc.).

**Task 4: Multiple Inheritance**
1. Create another class named **Motorcycle** that inherits from the **Vehicle** class.
2. Add a new attribute **engine_capacity** to the Motorcycle class (an integer representing the engine capacity in cc).

**Task 5: Private and Protected Variables**
1. Modify the Motorcycle class to include a private variable **__vin** and initialize it with **None** and a protected variable **_color** that is initialized with the help of the **set_color(self, color)** function.
2. Create a method named **get_vin(self)** in the Motorcycle class to return the **__vin** value.
3. Create a method named **set_vin(self, vin)** in the Motorcycle class to set the **__vin** attribute.

**Task 6: Generators in Python**
1. Create a generator function named **count_up_to()** that takes an integer parameter **‘n’** and generates numbers from 1 to that parameter.
2. Create another generator function named **fibonacci** that generates the Fibonacci sequence up to a specified limit **‘limit’**.

**Sample Output:**
```
Total vehicles: 3
Motorcycle color: Red
Motorcycle VIN: None
Counting up to 5:
1 2 3 4 5
Fibonacci sequence up to 50:
0 1 1 2 3 5 8 13 21 34 Total vehicles: 5
```

**Task 7: Testing**
1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
main.py
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|10|main.py file submitted and meets the program requirements |
|20|unit test passes test_vehicle_count|
|20|unit test passes test_motorcycle_vin|
