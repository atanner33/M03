#   Name: Alex Tanner
#   File_Name: GPA_Processor
#   Description: Proceess last name, first name, and GPA input. Will respond back with results of category they belong in. Will accept multiple inputs

endProgram = False

while endProgram == False:
    lastName = input("Enter the student's last name, or 'ZZZ' to terminate the program: ")
    if lastName == "ZZZ":
        print("Program terminated.")
        endProgram = True
    else:
        firstName = input("Enter the Student's first name: ")
        GPA = float(input("Enter the student's GPA: "))
        if GPA >= 3.5:
            print("Congrats!", firstName, lastName, "made the Dean's List.")
        elif GPA >= 3.25:
            print("Congrats!", firstName, lastName, "made Honor Roll.")
        else:
            print("Sorry,", firstName, lastName, "did not make Dean's List or Honor Roll.")