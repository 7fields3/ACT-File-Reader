import os

""" Take a location and use it to open a file. Return a LIST of the file. """


def file_string_splitter(flocation):
    file_open = open (flocation, "r")
    # .splitlines() splits the file at every \n (newline)
    split_file = file_open.read ().splitlines ()
    file_open.close ()
    return split_file


""" Return the string location of the file to be opened. """


def get_location(file):
    __location__ = os.path.realpath (os.path.join (os.getcwd (), os.path.dirname (__file__)))
    file_location = __location__ + "\\" + file
    return file_location


""" Ask for a file name and return the name string."""


def get_file_name():
    get_file = input ("Please type the name of the file "
                      "including the extension (for example, ACTSCORES.TXT):\n")
    return get_file


""" Calls personal_info and student_scores"""


def get_all_info():
    personal_info ()
    print ("---")
    student_scores ()


""" Gets student info """


def personal_info():
    # Last name, MI, First name
    print (entry[2:27], end="")
    print (entry[43], end="")
    print (" ", end="")
    print (entry[27:43])

    # Gender
    print ("Gender: ", end="")
    print (entry[87])

    # Date of birth
    print ("Date of birth: ", end="")
    print (entry[158:160], entry[160:162], entry[156:158])

    # Address
    print ("Address: ", end="")
    print (entry[44:84])
    print ("City: ", end="")
    print (entry[116:141])
    print ("State: ", end="")
    print (entry[143:145])
    print ("Zip code: ", end="")
    print (entry[145:150])

    # Phone number
    print ("Phone: ", end="")
    print (entry[106:116])

    # Student email
    print ("Email: ", end="")
    print (entry[550:600])

    # Grade level
    print ("Grade level: ", end="")
    print (entry[88:90])


""" Gets student scores """


def student_scores():
    # English Score
    print ("English: ", end="")
    print (entry[260:262])

    # Math score
    print ("Math: ", end="")
    print (entry[262:264])

    # Reading score
    print ("Reading: ", end="")
    print (entry[264:266])

    # Science score
    print ("Science: ", end="")
    print (entry[266:268])

    # Composite score
    print ("Composite: ", end="")
    print (entry[268:270])


""" Prints a string indicating the next record is being printed """


def next_record():
    print ("\n ******* NEXT RECORD *******\n")


# # Prints the pre-2015 writing section.
#     print(entry[162:178])
#
# # Prints the pre-2015 "standardized scores"?
#     print(entry[181:190])


# Gets the location of the file and puts it in a variable
file_list = file_string_splitter (get_location (get_file_name ()))

entry = ""
file_len = len (file_list)
count = 0

print ("This file contains {} student records.\n".format (file_len))
input ("Press ENTER to display.\n")
print ("******* BEGIN PRINTING RECORDS *******\n")

# Prints the records
for i in file_list:
    if (count + 1) in range (file_len):
        entry = i
        get_all_info ()
        next_record ()
        count += 1
    else:
        entry = i
        get_all_info ()
        print ("******* END OF FILE *******")

again = input ("\nPress ENTER to exit.")
