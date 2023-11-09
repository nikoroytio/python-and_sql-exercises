# OOP - File handling

Idea of this example is to look at the file handling by using Object-oriented principles within the Python programming language. Examples include **structural** way (no OOP applied) and a **oop** way implementation of file handling. OOP Example consists of `FileHandler` class which is used to create file handling objects that are suppose to make things more understandable.

## OOP - Example explained

In the examples folder there are 3 important files.

`main.py`, `file_handler.py` and `menu.py`.

Then there are 3 empty text files: `file1.txt`, `file2.txt` and `file3.txt`

The `main.py` is used to start the program. It defines the files in the project that can be used and also creates object `menu` from the `Menu` class that is defined in the `menu.py`.

The main program itself starts using the menu objects where the menu takes a certain role. It prompts user to make decisions in the program. Once the program has prompted file name and the operation for it, the main program calls the `runOperation` method from the `menu`. The `menu` object remembers all the decisions made previously and acts upon requests by calling `file_handler` object. It fills all the necessary parameters, so that the `file_handler` can do the required operations for the files themselves. If some key aspect is still missing, `runOperation` acts and prompts for the missing details, before proceeding with the method calls.

Once the `file_handler` object receives the call on some of the methods, it starts to work with the files as required. One aspect in the example is that it acts more like typical object, but `file_handlers` could work in a static way too. It means, that it doesn't have to maintain many states (property values) in the objects as most of the operations can be completed on their own, based on the method inputs. This static way might be implemented during the lecture.

## File operations

These examples have few operations:

1. print content
2. print content with row numbers
3. print line
4. add new line (append)
5. edit line

## Getting started

To test how the program now behaves, the structural program is ready for the use.

Open up the terminal and navigate to the example directory.

```bash
cd /path/to/project/examples/structural
python main.py
```

**!NOTE:** make sure the interpreter starts inside the "structural" directory, as it is the "working directory". There is no logic built to support any other paths.

Program starts and starts to ask for inputs:

```
python main.py 
Welcome to the file editor
Choose, which file you want to edit: 
1) file1.txt
2) file2.txt
3) file3.txt
Option: 
```

Insert integer between 1 and 3. Then press enter

```
Option: 1
You chose file: file1.txt
Select the operation you want to perform:
1) print content
2) print content with row numbers
3) print line
4) add new line (append)
5) edit line
Operation: 
```

Select operation by typing integer between 1 and 5. Then press enter

```
Operation: 1
File: file1.txt, content below:
#---FILE_START---#
Testi tiedosto
minun toinen rivi
minun kolmas rivi
#---FILE_END---#

Program exiting!
```

Choosing operation, it might ask for more questions. The above example options were `1` and `1`, which resulted into printing `file.txt` content into the terminal with some formatting around.

## Exercise 1

The first implementation of the OOP example is built during the class. It will use finnish terminology in every possible way. OOP Example will be built into the `examples/oop` directory. The files in the directory are:

- file1.txt
- file2.txt
- file3.txt
- main.py
- resurssien_hallinta.py
- valikko.py

Main program starts from the `main.py`, then responsibility of the functionalities are shifted to the `valikko.py`, while still keeping the program flow in the main program. Finally main program calls the `operaatioAjo` method from the `valikko` object and the `valikko` object still remembers the choices from the past (object states). `valikko` object uses the methods it has to call the `resurssien_hallinta` accordingly on each scenario. In the `resurssien_hallinta` object all the file handling operations are then handled and after the operations `resurssien_hallinta` returns void => interpreter goes back to the `valikko`, which does the same: returns void. Finally Python interpreter is back in the main program and can announce "Ohjelma päättyy!" before ending the program process.

## Exercise 2

Make a new example into the `examples` directory called `eng_oop`. Translate the existing **oop** example and try to improve the system. Think about all the namings in variables, classes, properties, methods, etc... Try to document the python code in english. Then try to improve atleast one existing program functionality and make one functionality on your own.

## Useful links

Here are some useful links with more fine details and examples about the file handling itself.

- Python 3 - ohjelmointiopas (Chapter 6): https://urn.fi/URN:ISBN:978-952-335-622-1
- IO - Core tools for working with streams https://docs.python.org/3/library/io.html