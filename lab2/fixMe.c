/* Lab 2 - Instructions
   
	1. Find and fix all the errors in this file.

	2. Leave a comment before each error that you fix explaining 
	   what the error was.

	3. Then copy the file into another file called  lab2.c  making 
	   sure to preserve fixMe.c (in case you need to refer to the 
		instructions again).

	4. Edit the header (these instructions) so that the proper header 
	   comment information is included in your file   lab2.c   which
		is the one that you will submit.
	
	5. After you have debugged and fixed the program, but before you 
	   submit your lab2.c file, test it with various numbers.  Use 2 
		(for triangle base) and 5 (for triangle height) as one of your 
		tests.  Notice the answer you get:
				Triangle area = (2 * triHeight) / 2 = 5 cm^2
		How would you change it so that the output says the following?
				Triangle area = (2 * 5) / 2 = 5 cm^2
		
	6. Do another test using 3 (for triangle base) and 5 (for triangle 
	   height) as one of your tests.  Notice the answer you get.  Leave 
		an additional comment at the bottom of your header comment showing 
		what answer you got when you used 3 and 5, and why that is. 

	7. After you have done all these steps and further testing,
	   then you can submit your
	   fixed lab2.c.  Your TA can help you if you have 
		trouble doing that.  
*/



/* Program description:
	This program asks the user to enter two numbers: one for the base of 
	a triangle, one for the height.  It then calculates the area of the 
	triangle and shows the results to the user.

	The scanf() function is used for user input and also comes from stdio.h
	like printf().
*/


#include <stdio.h>

int main (void) {

	int triBase = 0;
	int triHeight = 0;
	int triArea = 0:

	// Get user input
	print("Enter triangle base (cm): ")
	scanf("%d, &triBase);

	printf("Enter triangle height (cm): );
	scanf("%d", triHeight);

	/* Calculate triangle area
	triArea = (triBase * triHeight) / 2:

	// Print triangle base, height, area */
	printf("Triangle area = (");
	printf("%d" triBase);
	printf(" * ");
	printf(triHeight);
	printf(") / 2 = ");
	printf("%d", triArea);
	printf(" cm^2\n");

	return 0;
}



