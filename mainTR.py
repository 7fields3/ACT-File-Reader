import os

# Multiply these by the desired line number to get results for that line.
# e.x. line 0 = (1050 * 0) = 0, so just use the default values.
magicNumber = 1050
magicNumber1 = 1051

""" Opens a file and return a string. """
def string_returner(flocation):
    fileopen = open(flocation, "r")
    strungfile = fileopen.read()
    fileopen.close()
    return strungfile

""" Return the string location of the file to be opened. """
def get_location(file):
    __location__ = os.path.realpath (
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_location = __location__ + "\\" + file
    return file_location


""" Return the string name of the file to be opened."""
def get_file_name():
    getFile = input("Please type the name of the file "
                    "including the extenstion (for example, ACTSCORES.TXT):\n")
    return getFile


""" Return the length of the file."""
def file_len(fname):
    fileLength = 0
    for i, l in enumerate(fname):
        fileLength += 1
    return fileLength


def get_all_info():
    get_name()
    stu_gender()
    date_of_birth()
    stu_address()
    phone_number()
    student_email()
    grade_level()
    old_writing_results()
    old_std_scores()
    composite_score()
    english_score()
    math_score()
    reading_score()
    science_score()


""" The first number is +1051 and the second is +1050. If there's only one, it's +1050.
    For whatever reason, the pdf that the base numbers came from isn't totally accurate.
    It's probably just me though."""
def get_name():
    print(fileString[(2 + (magicNumber1 * whichLine)):(27 + (magicNumber * whichLine))], end="")
    print(fileString[44 + (magicNumber * whichLine)], end="")
    print(" ", end="")
    print(fileString[(27 + (magicNumber1 * whichLine)):(43 + (magicNumber * whichLine))])

def stu_address():
    print("Address: ", end="")
    print(fileString[(44 + (magicNumber1 * whichLine)):(84 + (magicNumber * whichLine))])
    print("City: ", end="")
    print(fileString[(116 + (magicNumber1 * whichLine)):(141 + (magicNumber * whichLine))])
    print("State: ", end="")
    print(fileString[(143 + (magicNumber1 * whichLine)):(145 + (magicNumber1 * whichLine))])
    print("Zip code: ", end="")
    print(fileString[(145 + (magicNumber1 * whichLine)):(154 + (magicNumber * whichLine))])

def stu_gender():
    print("Gender: ", end="")
    print(fileString[(87 + (magicNumber1 * whichLine))])

def grade_level():
    print("Grade level: ", end="")
    print(fileString[(88 + (magicNumber1 * whichLine)):(90 + (magicNumber1 * whichLine))])

def phone_number():
    print("Phone: ", end="")
    print(fileString[(106 + (magicNumber1 * whichLine)):(116 + (magicNumber1 * whichLine))])

def date_of_birth():
    print("Date of birth: ", end="")
    print(fileString[(158 + (magicNumber1 * whichLine)):(160 + (magicNumber1 * whichLine))],
          fileString[(160 + (magicNumber1 * whichLine)):(162 + (magicNumber1 * whichLine))],
          fileString[(156 + (magicNumber1 * whichLine)):(158 + (magicNumber1 * whichLine))])

# Prints the entire section. Only for tests taken Pre-2015.
def old_writing_results():
    print(fileString[(162 + (magicNumber1 * whichLine)):(178 + (magicNumber * whichLine))])

# Prints the entire section. Only for tests taken Pre-2015?
def old_std_scores():
    print(fileString[(181 + (magicNumber1 * whichLine)):(190 + (magicNumber * whichLine))])

def english_score():
    print("English: ", end="")
    print(fileString[(260 + (magicNumber1 * whichLine)):(262 + (magicNumber1 * whichLine))])

def math_score():
    print("Math: ", end="")
    print(fileString[(262 + (magicNumber1 * whichLine)):(264 + (magicNumber1 * whichLine))])

def reading_score():
    print("Reading: ", end="")
    print(fileString[(264 + (magicNumber1 * whichLine)):(266 + (magicNumber1 * whichLine))])

def science_score():
    print("Science: ", end="")
    print(fileString[(266 + (magicNumber1 * whichLine)):(268 + (magicNumber1 * whichLine))])

def composite_score():
    print("Composite: ", end="")
    print(fileString[(268 + (magicNumber1 * whichLine)):(270 + (magicNumber1 * whichLine))])

def student_email():
    print("Email: ", end="")
    print(fileString[(550 + (magicNumber1 * whichLine)):(600 + (magicNumber * whichLine))])

def next_record():
    print("\n ******* NEXT RECORD *******\n")



# Get the length of the file
fileLength = 0
fileLength -= 1
whichLine = 0

fileString = string_returner(get_location(get_file_name()))

for line in fileString.splitlines():
    fileLength += 1




# This is the main code. NTS, make everything above into a class that automatically executes the
# functions.
while whichLine < fileLength:
    print("This file contains {} student records.\n".format(fileLength))
    input("Press ENTER to display.\n")
    print("\n******* BEGIN PRINTING RECORDS *******\n")
    for i in range(fileLength):
        if (i + 1) in range(fileLength):
            get_all_info()
            whichLine = whichLine + 1
            next_record()
        else:
            get_all_info()
            whichLine = whichLine + 1
            print("******* END OF FILE *******")


input("\nPress ENTER to exit.")
