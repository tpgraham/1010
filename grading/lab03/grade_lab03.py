"""
This is a script specific to grading Lab03 of CPSC 1011 (Spring 2017).
"""
import sys
import os
import glob
import subprocess
import logging
import traceback
import math

from subprocess import Popen, PIPE

def check_lab_output (lines, logging, totalPoints) :

    subGrade = 0.0
    textPts = (6.0/60.0) * totalPoints
    linePts = (4.0/60.0) * totalPoints

    ansLines = ["intVar1 = 4  and intVar2 = 3\n", \
        "\n", \
        "Expression values are:\n", \
        "exp1 = 24\n", \
        "exp2 = 2\n", \
        "\n", \
        "intVar3 = 3 and intVar4 = 5\n", \
        "\n", \
        "Expression values are:\n", \
        "exp3 = 5\n", \
        "exp4 = 1\n"]

    try :
        for i, ansLine in enumerate(ansLines):
            pts = linePts if ansLine == "\n" else textPts
            if lines[i].count(ansLine) == 1 \
                or lines[i].count(ansLine.replace("  ", " ")) == 1 : #the answer key has two spaces, but some people put one space
                subGrade += pts
                logging.info("Gained " + str(pts) + " pts for printing correct Line " + str(i))    
            else :
                logging.info("Lost " + str(pts) + " pts for printing incorrect Line " + str(i))
                logging.info("Correct:" + ansLine)
                logging.info("Incorrect:" + lines[i])
    except :
        logging.error("Error during checking lab output");
        #traceback.print_exc()

    return (subGrade)

def main (argv) :
   
    # find user file, will only find lab1.c or lab1-n.c (n being a version number)
    student_id = sys.argv[1]
    files = glob.glob("submissions/*_" + student_id + "_*lab3*.c")
    outputfiles = glob.glob("submissions/*_" + student_id + "_*output*.txt")
    technical_grade = 0
    
    # set up logging for the grading process of the student
    try :
        # strip ".c" extension off the file name so we can use it for the log name
        cutoff = files[0].index(".")
        file_name = files[0][len("submissions/"):cutoff]

        log_name = "logs/" + file_name + ".log"
        logging.basicConfig(filename=log_name, level=logging.INFO, filemode='w')

        #logging.info("Received 10 points for correctly naming file") 
        #technical_grade = technical_grade + 10
    except :
        logging.error("No .c file with expected name, perhaps file is mis-named.")
        sys.exit(0)

    # check for the output.txt
    try :
        # strip ".txt" extension off the outoput file name 
        cutoff = outputfiles[0].index(".")
        outputfile_name = outputfiles[0][:]

        technical_grade += 4
        logging.info("Received 4 points for correctly output file") 
    except :
        logging.error("No .txt file with expected name, perhaps file is mis-named.")
        sys.exit(0)

    # attempt grading
    try :
        compile_result = subprocess.check_call(["gcc", \
                                                files[0], "-o", \
                                                "execs/" + file_name])

        logging.info("Program successfully compiled.")

        try :
            #p = Popen(["./execs/" + file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE);
            #exec_result, stderr = p.communicate(os.linesep.join(["4", "5"]));
            exec_result = subprocess.check_output(["./execs/" + file_name])
            logging.info("Program finished executing.")
            
            exec_lines = exec_result.splitlines(True)
            technical_grade += check_lab_output(exec_lines, logging, 60.0)
        except :
            logging.error("Program failed to execute properly.")
            #traceback.print_exc()

        try :
            #p = Popen(["./execs/" + file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE);
            #exec_result, stderr = p.communicate(os.linesep.join(["3", "5"]));
            #exec_result = subprocess.check_output(["./execs/" + file_name])
            #logging.info("Program finished executing.")
            with open(files[0]) as f :
                code_lines = f.read()

            if code_lines.count("fprintf") >= 1 : 
                technical_grade += 6
                logging.info("Gained 6 pts for using fprintf at least once")
            else : 
                logging.info("Lost 6 pts for not using fprintf at least once")

            if code_lines.count("fprintf") >= 4 : 
                technical_grade += 4
                logging.info("Gained 4 pts for using fprintf at least four times")
            else : 
                logging.info("Lost 4 pts for not using fprintf at least four times")
        except :
            logging.error("Code failed to open properly.")
            #traceback.print_exc()

        try :
            #p = Popen(["./execs/" + file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE);
            #exec_result, stderr = p.communicate(os.linesep.join(["3", "5"]));
            #exec_result = subprocess.check_output(["./execs/" + file_name])
            #logging.info("Program finished executing.")
            with open(outputfile_name) as f :
                output_lines = f.readlines()

            technical_grade += check_lab_output(output_lines, logging, 6.0)
        except :
            logging.error("Output failed to open properly.")
            #traceback.print_exc()
    except :
        logging.error("Program failed to compile properly.")
        #traceback.print_exc()

    # round up if the grade is a decimal number
    technical_grade = math.ceil(technical_grade)
    print technical_grade

    return(0)

if __name__ == "__main__":
    main(sys.argv[1:])
