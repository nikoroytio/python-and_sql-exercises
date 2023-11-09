
from fileinput import filename
from importlib.metadata import files
from typing import List
from file_handling import fileHandling
import os

A = True

class Menu:

    """
    The class works and remembers selected things,
    and offers menu functionality

    """
    files: List[str] = []

    # fileIndex is a property, i.e. a "variable" of an object"
    fileIndex = -1
    file_handling: fileHandling

    def __init__(self, files) -> None:
        # print(self.files)
        self.files = files
        # print(self.files)
        self.file_handling = fileHandling()
    
    def filename(self):
        return self.files[self.fileIndex]

    def fileSelect(self):
        """
        This menu method is used to select a file
        """
        print("Select the file you want to process: ")
        for i in range(len(self.files)):
            print(str(i + 1) + ") " + self.files[i])
        # information about the selection is stored in the object. The information could also be returned
        self.fileIndex = int(input("Enter selection: ")) - 1
        print("You selected a file: " + self.files[self.fileIndex])

    def operationSelect(self):
        """
        This menu method is used to select the operation to be performed on the file
        """
        print("\nChoose an operation:")
        print("1) Print the contents of the file")
        print("2) Print the contents of the file with the line number")
        print("3) Print single line")
        print("4) Add line after file")
        print("5) Overwrite line")
        print("6 Delete file")
        self._fileOpeeratio = int(input("Enter selection: ")) - 1
        print("Your selected operation: " + str(self._fileOpeeratio + 1))
    
    def operationRun(self, external=-1):
        """
        _operation without "self beginning means,
        that the feature is only used during the "operationRun" method
        """
        _operation = self._fileOpeeratio
        if (external != -1): # run external
            _operation = external
    
        
        # The necessary parameters are precisely defined below, collected if missing
        # Trying the selection structure with "match" instead of "if-elif-elif".

        match _operation:
            case 0: # 0 = 1) Print the contents of the file
                self.file_handling.printAll(self.files[self.fileIndex])
            case 1: # 1 = 2) Print the contents of the file with line numbers
                self.file_handling.printLinesWithNumbers(self.filename())
            case 2: # 2 = 3) Print a single line
                lineIndex = int(input("Enter line number: ")) - 1
                self.file_handling.printOneline(self.filename(), lineIndex)
            case 3: # 3 = 4) Add a line after the file
                yote = input("Enter the content of the line: ")
                self.file_handling.continueFile(self.filename(), input)
            case 4: # 4 = 5) Overwrite the line
                yote = input("Enter the content of the line: ")
                lineIndex = int(input("Enter line number: ")) - 1
                self.file_handling.overwriteLine(self.filename(), lineIndex, input)
            case 5: #deletes file
                name = self.filename()
                myFile = "/koulu/Oliot ja tietokannat 2022/viikko4/L4-master/examples/oop/oop_eng/{0}".format(name)
                if os.path.isfile(myFile):
                    os.remove(myFile)
                else:    ## Show an error ##
                    print("Error: %s file not found" % myFile)
            case _:
                print("The operation is not in the supported list")

