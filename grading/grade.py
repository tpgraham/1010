import csv
import sys
import subprocess
import os

"""
This function calls the python script specific to grading each lab and uses
the returned output as the student's technical grade.

NOTE - the grading scripts should ONLY output the grade. Everything else needs
to be logged or printed to a different stream.
"""
def getGrade(program, student) :
    student_name = student[0] 

    # run the student's program
    student_id = student[1]
    program_output = subprocess.check_output(["python", program, student_id])

    try :
        result = int(program_output)
    except :
        result = 0

    print student_name , " - ", result

    return result

"""
Returns the index where we should insert our grades.

In the auxiliary grade book, every lab grade has three components :
1. technical (determined by getGrade() in this same module)
2. non-technical (style and other points determined manually)
3. the final grade (technical and non-technical combined)

This function takes the existing auxiliary headers and makes sure we have the 
columns we need to write out our results.

NOTE - this will update the CSV header if needed, as a side effect.
"""
def getLabIndex(csv_header, lab_num) :
    lab_name = "lab" + lab_num
   
    # make sure all the headers for our lab are in place and good to go 
    header_count = int(csv_header.count(lab_name + "-technical")) + \
                    int(csv_header.count(lab_name + "-non-technical"))  + \
                    int(csv_header.count(lab_name + "-final"))
    
    # make sure our CSV file isn't messed up -- all or none of the lab headers
    # ought to be there (three total -- technical, non-technical, and final)
    if header_count != 0 and header_count != 3 :
        sys.stderr.write("ERROR - CSV file aux_grades.csv has incorrect headers\n")
        sys.stderr.write("ERROR - " + str(header_count) + " lab headers found\n")
        sys.exit(1)

    if header_count == 0 :
        csv_header.append(lab_name + "-technical")
        csv_header.append(lab_name + "-non-technical")
        csv_header.append(lab_name + "-final")
    
    else :
        # Make sure the headers for this lab follow each other sequentially
        assert(csv_header.index(lab_name + "-technical") + 1 == \
                csv_header.index(lab_name + "-non-technical"))
     
        assert(csv_header.index(lab_name + "-non-technical") + 1 == \
                csv_header.index(lab_name + "-final"))

    # This is the index where we should insert technical grades in the aux csv file
    return csv_header.index(lab_name + "-technical")    

"""
This program follows a series of steps to automate lab grading :

1. For every student, pass his/her id to the grading script (from a CSV file).
2. Retrieve the student score from the grading script (see individual
   grading scripts for more details on how each lab is graded.
3. Write results to the CSV file.
"""
def main (argv) :
    # Parse arguments
    lab_num = "-1"

    if len(sys.argv) < 2 :
        print "usage : grade.py <lab_number> " 
        sys.exit(-1)
    else :
        args = sys.argv
        lab_num = args[1]

        # ensure consistency
        if int(lab_num) < 10 :
            lab_num = "0" + str(int(lab_num))

        print "Grading Lab ", lab_num

    # Read in Aux CSV to write grades to
    aux_grades = "aux_grades.csv" 
    program = "grade_lab" + str(lab_num) + ".py" 
    
    with open(aux_grades) as r :
        rows = []

        for row in csv.reader(r) :
            rows.append(row)
    
        # Set working directory to lab folder for testing
        os.chdir("lab" + lab_num + "/")    
        
        lab_index = getLabIndex(rows[0], lab_num)
 
       # Go through the CSV rows, get student ID, and use it to grade their program. 
        for i in range (1, len(rows)) :

            student  = rows[i][:2] # pass student name, student id
            technical_grade = getGrade(program, student)

            # touch up the CSV rows so our values insert cleanly           
            while len(rows[i]) <= lab_index + 2:
                rows[i].append(0)
             
            rows[i][lab_index] =  technical_grade

    # Write results to csv
    os.chdir("..")    
    with open("aux_grades.csv", 'w') as w :
        writer = csv.writer(w)
        writer.writerows(rows)

        print "Saved results successfully"

if __name__ == "__main__":
   main(sys.argv[1:])
