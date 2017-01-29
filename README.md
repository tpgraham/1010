# Grading Scripts for CPSC 1011 Spring 2017

The grading repository has a collection of pretty straightforward python scripts for the automation of compiling and executing student grades, and updating an auxiliary gradebook with those scores so it can be merged with the master gradebook later (and consequently uploaded to Canvas).

## Simple Set up For Automated Lab Grading
1. In the **grading** folder, create a new directory for the lab you wish to grade
    * Format of directory name : "lab" + lab\_number \(01, 09, 13, 22, etc\)
2. Create a script for the lab you want to grade 
    * Essentially, make a script that applies some rubric and outputs the grade to stdout
    * Format of lab name : "grade\_lab" + lab\_number + ".py" \(same number as before\)
    * Of course, there's a lot of code in the **grade\_lab01.py** script that could be repurposed
3. Download student submissions from Canvas \(zip file\)
4. Run the initial grading script as % python grade.py \[lab\_number\]
5. After adding non-automated points \(i.e., checking for style, etc\), run % merge.py \[lab\_number\] \[path\_to\_master\] to add the grade components and save the results.

**Note** - Point 2 is pretty abstract. The details of logging, file management, and other details are basically left up to whoever is writing the script grading that week's lab. All **grade.py** cares about is that the standard output of the script is a number it can pasre into the student's technical grade.

## Further Improvements That Could Be Added
* Resolution for student's incorrectly-named-files in the lab grading scripts. In the script for lab01, for example, if the student's file isn't found a grade of 0 is received, so that leads to more hand-checking down the line
* figuring out exactly how robust the format of the master CSV file is when we upload it to Canvas
* Other things probably... 
