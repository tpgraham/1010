/*
    Mary Glenn
    CPSC 1011 - 002
    Lab 2 - Debugging
    Spring 2017
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

    // ERROR - should be a semicolon, not a colon
	int triArea = 0;

	// Get user input, add a semicolon
    // ERROR - should be printf
	printf("Enter triangle base (cm): ");

    // ERROR - first paramter of scanf() is missing quotations
	scanf("%d", &triBase);

    // ERROR - printf() is missing a quotation before the closing parantheses.
	printf("Enter triangle height (cm): ");
    // ERROR - triHeight's address not passed in scanf
	scanf("%d", &triHeight);

	/* Calculate triangle area */
    // ERROR - complete comment, and should have a semicolon before
	triArea = (int)((triBase * triHeight) / 2);

	// Print triangle base, height, area */
	printf("Triangle area = (");

    // ERROR - add comma
	printf("%d", triBase);
	printf(" * ");
	printf("%d", triHeight);
	printf(") / 2 = ");
	printf("%d", triArea);
	printf(" cm^2\n");

	return 0;
}



