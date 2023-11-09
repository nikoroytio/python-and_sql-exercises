# Run this file only from the same directory (working directory = this directory)

# File handling in a structural way
tiedostot = [
    'file1.txt',
    'file2.txt',
    'file3.txt'
]

## Main program
print("Welcome to the file editor")
print("Choose, which file you want to edit: ")
print("1) file1.txt")
print("2) file2.txt")
print("3) file3.txt")
# Users prefer counting from 1, programs prefer 0
tiedostoIndeksi = int(input("Option: ")) - 1 # hence the -1

print(f"You chose file: {tiedostot[tiedostoIndeksi]}")
print("Select the operation you want to perform:")
print("1) print content")
print("2) print content with row numbers")
print("3) print line")
print("4) add new line (append)")
print("5) edit line")
tiedostoOperaatio = int(input("Operation: "))

if (tiedostoOperaatio == 1):
    print("File:", tiedostot[tiedostoIndeksi] + ', content below:')
    tiedosto = open(tiedostot[tiedostoIndeksi], 'r')
    print("#---FILE_START---#")
    for rivi in tiedosto:
        # file rows have control character \n in the end
        # control characters are interpreted differently than normal characters
        # in this case \n is a new line character
        # print command has ending character \n by default
        # so below we want to get rid of the double \n\n somehow.
        print(rivi, end='') # solved by defining empty string in print end parameter
    print("#---FILE_END---#")
elif (tiedostoOperaatio == 2):
    print("File:", tiedostot[tiedostoIndeksi] + ', content below with row nums:')
    tiedosto = open(tiedostot[tiedostoIndeksi], 'r')
    tiedosto = tiedosto.readlines()
    # Looping through indexes to get row numbers
    print("#---FILE_START---#")
    for i in range(len(tiedosto)):
        print("Row " + str(i + 1) + ":", tiedosto[i], end='')
    print("#---FILE_END---#")
elif (tiedostoOperaatio == 3):
    # User selects row number starting from 1
    rivi_numero = int(input("Select line number to be printed: ")) - 1 # indexes starts from 0
    tiedosto = open(tiedostot[tiedostoIndeksi], 'r').readlines() # list of lines/rows
    print("printing line number: " + str(rivi_numero + 1))
    print(tiedosto[rivi_numero], end='')
elif (tiedostoOperaatio == 4):
    # input data type is string
    new_line = input("Insert new line: ")
    # string can be written to a file
    # a is for append
    tiedosto = open(tiedostot[tiedostoIndeksi], 'a').write('\n' + new_line)
    # tiedosto.close() # old method does not exist anymore?
    print("Line inserted into the file.")
elif (tiedostoOperaatio == 5):
    # w is for write, which over writes the whole file with content
    # r is for read
    # Can't mix them together, hence two file opening methods
    tiedosto = open(tiedostot[tiedostoIndeksi], 'r')
    rivit = tiedosto.readlines()
    muokattavanRivinIndeksi = int(input("Line to edit: "))
    muokattuRivi = input("New line content: ")

    # Filling missing lines, if line to be editted doesn't exist
    # if line to be editted is the last existing row, the value is 1 smaller than the rows length
    # e.g. rows[4] is the last item in rows => len(rows) == 5
    if (muokattavanRivinIndeksi >= (len(rivit))):
        # same has to be accounted in the rows range
        for rivinIndeksi in range(muokattavanRivinIndeksi + 1):
            if (len(rivit) <= rivinIndeksi):
                rivit.append('\n') # adding empty row to the list
            #else: # else is not required, it would mean filling the same thing
            #    # rivit[rivinIndeksi] = rivit[rivinIndeksi]
    # Editting the line which user wanted to edit
    rivit[muokattavanRivinIndeksi] =  muokattuRivi + '\n'
    tiedosto.close()
    tiedostoon = open(tiedostot[tiedostoIndeksi], 'w')
    # print(rivit)
    for r in rivit:
        tiedostoon.write(r)
    tiedostoon.close()
else:
    print("Unknown operation")

print("", end='\n')
print("Program exiting!")