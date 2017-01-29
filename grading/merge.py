"""
A simple module for calculating final lab grades and putting them into the master 
grade file (.CSV).
"""
import sys
import csv

def main (argv) :
    lab_num = -1
    master_grades = "/"

    # Parse Arguments
    if len(sys.argv) < 3 :
        print "usage : merge.py <lab_number> <path_to_master_csv>"
        sys.exit(2)
    else :
        args = sys.argv
        lab_num = args[1]
        master_grades = args[2]
        print "Writing results of Lab", lab_num , " to ", master_grades  

    # Open Master and Auxiliary CSV Files
    aux_grades = "aux_grades.csv" 
    with open(aux_grades) as a :
        rows_a = []   
        for row_a in csv.reader(a) :
            rows_a.append(row_a)

    with open(master_grades) as m :
        rows_m = []
        for row_m in csv.reader(m) :
            rows_m.append(row_m)    

    index = 1 # skip over headers
    header = "lab" + lab_num + "-technical"

    technical_grade_index = rows_a[0].index(header)
    style_grade_index = technical_grade_index + 1
    final_grade_index = style_grade_index + 1

    # Find where in the master csv we need to insert final grades    
    section_index = 3
    master_final_index = 0
    while master_final_index < len(rows_m[0]) :
        try :
            if rows_m[0][master_final_index].index("Lab " + str(lab_num)) == 0 :
                break
        except :
            master_final_index += 1


    # Calculate final grades and log it in the aux and master CSVs 
    while index < len(rows_a) and index < len(rows_m) :

        # verify student 
        if rows_a[index][0] != rows_m[index][0] :
            sys.stderr.write("ERROR - student lists mis-matched!\n")
            sys.exit(2)

        if rows_a[index][section_index].count("-004") == 1 :
            final_grade = 0 # don't assign a grade
        else : 
            final_grade = int(rows_a[index][technical_grade_index]) + \
                                        int(rows_a[index][style_grade_index]) 

        rows_a[index][final_grade_index] = final_grade
        rows_m[index][master_final_index] = final_grade

        index = index + 1
 
    # Update Master CSV
    with open(master_grades, 'w') as w :
        writer = csv.writer(w)
        writer.writerows(rows_m)

    w.close()

    with open(aux_grades, 'w') as w :
        writer = csv.writer(w)
        writer.writerows(rows_a)

    print "Successfully wrote results"

if __name__ == "__main__":
   main(sys.argv[1:])
