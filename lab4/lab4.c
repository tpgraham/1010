#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {

    double N;
    double guess;
    double startingGuess;

    // collect user input
    printf("Enter a N : ");
    scanf("%lf", &N);
    printf("Enter a starting guess: ");
    scanf("%lf", &guess);

    double squareRoot = sqrt(N);

    printf("\nThe square root of %lf is %lf\n\n", N, squareRoot); 

    // calculate square root using babylonian method
    int k = 0;
    startingGuess = guess;

    while (fabs(sqrt(N) - guess) >= 5e-7) {
        guess = 0.5 * (guess + (N/guess));
        k += 1;
        printf("step\t%d:\t%lf\n", k, guess);
    }

    printf("\nUsing the Babylonian method, the square root of %.0lf with a ", N);
    printf("starting guess of %0.0lf was found in %d steps.\n", startingGuess, k); 

    return 0;
}
