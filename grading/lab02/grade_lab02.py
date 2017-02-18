"""
This is a script specific to grading Lab01 of CPSC 1011 (Spring 2017).
"""
import sys
import os
import glob
import subprocess
import logging

from subprocess import Popen, PIPE

def main (argv) :
   
    # find user file, will only find lab1.c or lab1-n.c (n being a version number)
    student_id = sys.argv[1]
    files = glob.glob("submissions/*_" + student_id + "_*lab1*.c")
    technical_grade = 0
    
    # set up logging for the grading process of the student
    try :
        # strip ".c" extension off the file name so we can use it for the log name
        cutoff = files[0].index(".")
        file_name = files[0][len("submissions/"):cutoff]

        log_name = "logs/" + file_name + ".log"
        logging.basicConfig(filename=log_name, level=logging.INFO, filemode='w')

        logging.info("Received 10 points for correctly naming file") 
        technical_grade = technical_grade + 10
    except :
        logging.error("No file with expected name, perhaps file is mis-named.")
        sys.exit(0)

    # attempt grading
    try :
        compile_result = subprocess.check_call(["gcc", \
                                                files[0], "-o", \
                                                "execs/" + file_name])

        logging.info("Program successfully compiled.")

        try :
            p = Popen(["./execs/" + file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE);
            exec_result, stderr = p.communicate(os.linesep.join(["4", "5"]));
            #exec_result = subprocess.check_output(["./execs/" + file_name])
            logging.info("Program finished executing.")

            if exec_result.count("10") == 1 and \
                                exec_result.count("4") == 1 and \
                                exec_result.count("5") == 1 :
                logging.info("Received 50 pts for printing 4 * 5 / 2 = 10 correctly")
                technical_grade = technical_grade + 50
            else :
                logging.info("Lost 50 pts for printing 4 * 5 / 2 = 10 incorrectly")

        except :
            logging.error("Program failed to execute properly.")

        try :
            p = Popen(["./execs/" + file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE);
            exec_result, stderr = p.communicate(os.linesep.join(["3", "5"]));
            #exec_result = subprocess.check_output(["./execs/" + file_name])
            logging.info("Program finished executing.")

            if exec_result.count("7.5") == 0 and exec_result.count("7") == 1 and \
                                exec_result.count("3") == 1 and \
                                exec_result.count("5") == 1 :
                logging.info("Received 50 pts for printing 3 * 5 / 2 = 7 correctly")
                technical_grade = technical_grade + 50
            else :
                logging.info("Lost 50 pts for printing 3 * 5 / 2 = 7 incorrectly")
        except :
            logging.error("Program failed to execute properly.")
    except :
        logging.error("Program failed to compile properly.")

    print technical_grade

    return(0)

if __name__ == "__main__":
    main(sys.argv[1:])
