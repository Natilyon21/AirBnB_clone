
Description
===============================
AirnBnB is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.
The project currently only implements the back-end console.

Consol
===============================
The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate 
all classes utilized by the application (achieved by calls on the storage object defined above).The AirBnB console can be run both 
interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file 
console.py at the command line.

Console Commands
===============================
The AirBnB console supports the following commands:

*create
Usage: create <class>

Creates a new instance of a given class
  
*show
Usage: show <class> <id> 

Prints the string representation of a class instance based on a given id
  
*destroy
Usage: destroy <class> <id>

Deletes a class instance based on a given id

*all
Usage: all or all <class>

Prints the string representations of all instances of a given class
  
*count
Usage: count <class> or <class>.count()
 
Retrieves the number of instances of a given class
  
*update
Usage: update <class> <id> <attribute name> "<attribute value>"
  
Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs.
  
Testing 
===============================
Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

$ python3 unittest -m discover tests
  
Author
===============================
Name -
  NATNAEL SEWAGEGN
  
Email
  <radking400@gmail.com>
