
"""
This class can handle the printing of a file,
and can make basic edits to files based on user inputs.
The file demonstrates how files can be handled using the object paradigm.
"""
class fileHandling:
    def __init__(self) -> None:
        print("Resource manager created")
    
    def printAll(self, file_name: str):
        file = open(file_name, 'r')
        print("\nFile:", file_name, sep=' ')
        print("\n#---FILE_BEGIN---#")
        print(file.read(), end='') # remove the \n control character from the "end" parameter
        print("\n#---END OF FILE---#")

    def printLinesWithNumbers(self, file_name: str):
        # print("Not working yet.")
        file = open(file_name, 'r').readlines()
        print("\nFile:", file_name, sep=' ')
        print("\n#---FILE_BEGIN---#")
        for lineIndex in range(len(file)):
            # it is taken into account that there is a \n specification at the end of the lines, so that it is not repeated in the output
            print("LINE " + str(lineIndex + 1) + ": " + file[lineIndex], end='')
        print("\n#---END OF FILE---#")

    def printOneline(self, file_name: str, line_index: int):
        # print("Not working yet.")
        file = open(file_name, 'r').readlines()
        print("\nFile:", file_name, sep=' ')
        for i in range(len(file)):
            if i == line_index:
                print(file[i])
        print("")

    def continueFile(self, file_name: str, string: str):
        # print("Not working yet.")
        file = open(file_name, 'a')
        file.write('\n' + string)
        print("line added!")

    """
    Let's edit line X of the file. If the line doesn't exist, this creates it.
    For overwriting, the parameter "string" is used to replace the lines of the file
    the one pointed to by the "lineIndex" parameter.
    """
    def overwriteLine(self, file_name: str, editableLineIndex: int, string: str):
        """
        'w' means file overwrite
        'r' stands for reading the file 'read'
        The two states cannot be confused. Either read or write.
        """
        file = open(file_name, 'r')
        lines = file.readlines()
        editedLine = string

        """
        Creates a line if it doesn't exist.
        If the line is the last line to be written, then
        In this case, remember that the index of the last line is one
        less than the length of the line list "len(lines)".
        E.g. lines[5] is the last item in the list, then "len(lines)" is 6
        """
        if (editableLineIndex >= (len(lines))):
            # the size of the value set must also be taken into account
            for lineIndex in range(editableLineIndex + 1):
                if (len(lines) <= lineIndex):
                    lines.append('\n') # add the missing empty line
                # else is not needed because it is an existing line
        # Editing is done for the line that the user wants
        lines[editableLineIndex] = '\n' + editedLine
        to_file = open(file_name, 'w')

        for line in lines:
            to_file.write(line)
        
        to_file.close()
