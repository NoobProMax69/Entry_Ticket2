# Entry_Ticket2

## Description

The task

You have been selected to help a group of scientists who are currently investigating whether there is a link between light exercise and oral health in elderly people. The group needs you to create a Python script that can help them record the time it takes the different test subjects to complete a lap around a nearby lake.


The script shall be responsible for recording some data each time a test subject passes the finish line, and shall also have functionality for storing the recorded data to a text file, load data about test subjects that has completed the lap around the lake from a text file, and to display the currently known data about the test subjects to the user of the script.  

There are some quite strict parameters for you to adhere to when developing the script as the scientists have already agreed on both the user interface and the internal structure of the script with some external partners. This videoLinks to an external site. is a representation of how the scientists want the script to work and look like when finished, and this Python scriptLinks to an external site. was provided as a template of sorts for how the internal structure must look like. Below is a detailed description of how each function shall work. 

print_menu()
Shall not take any parameters and is responsible for displaying a menu to the user that looks exactly like the example below. The header line shall have nine dashes before the word Menu and ten dashes after, and the separator line after the menu options shall have 25 dashes.

--------- Menu ----------
a) Add a new test subject
s) Show all information
r) Read from file
w) Write to file
q) Quit
-------------------------
new_test_subject()
This function takes no parameters but returns a tuple with two elements. The returned tuple shall consist of a string representing the number assigned to a test subject and an integer representing how many minutes it took the test subject to complete a lap around the lake. Both the number and time shall be read from the user/keyboard before the tuple is constructed and returned. 

write_data(test_subjects, filename)
The test_subjects parameter is a list of tuples containing data about all the test subjects and filename is a string. The function shall open the text file filename in write mode and write all data from test_subjects to the file before it is closed again. Each tuple from test_subjects shall take up two lines in the file where the first line is the number assigned to a test subject and the second line is the time it took that test subject to complete a lap around the lake.

read_data(filename)
This function shall use the parameter filename to open a text file, read all the records in the file, and return a list of tuples. Each record in the file takes up two lines where the first line is the number assigned to a test subject and the second line is the time it took that test subject to complete a lap around the lake. After every read record, number and time, a tuple shall be constructed and added to the list that is returned after all tuples are read. Each tuple shall have two elements, the number as a string and the time as an integer.

print_test_subjects(test_subjects)
Uses the test_subjects list that contains tuples, each storing number and time, to print information about all the test subjects using the format shown below where the colons are aligned, the numbers and time have a minimum width of 5 characters, and where there is an empty line without any spaces, tabs, or other characters between the output of each test subject.

---- Registered test subjects ----
Number :   10
Time   :   23

Number :   20
Time   :   29
main()
Shall contain a loop that displays the menu, that allows the user to select an option from the menu, and handle each menu option. The first option shall use the function for reading data about a new test subject and add the returned tuple to a current list. The second option shall call the function for displaying all test subjects using the current list an argument. As for the next two options they are similar in that they first ask the user for a filename and then either read the data from the specified file and store the returned list as the current list of test subjects or write the current list of test subjects to the specified file. After having either read or written data from/to the file a message shall be displayed to the user using the format below and where read from is replaced by written to if that menu option was used:
*** Data read from file ***