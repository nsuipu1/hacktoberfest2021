// C program for the above approach

#include <stdio.h>

// Function to return the
// minimum of two numbers
int Min(int Num1, int Num2)
{
	return Num1 >= Num2
			? Num2
			: Num1;
}

// Utility function to calculate LCM
// of two numbers using recursion
int LCMUtil(int Num1, int Num2, int K)
{
	// If either of the two numbers
	// is 1, return their product
	if (Num1 == 1 || Num2 == 1)
		return Num1 * Num2;

	// If both the numbers are equal
	if (Num1 == Num2)
		return Num1;

	// If K is smaller than the
	// minimum of the two numbers
	if (K <= Min(Num1, Num2)) {

		// Checks if both numbers are
		// divisible by K or not
		if (Num1 % K == 0 && Num2 % K == 0) {

			// Recursively call LCM() function
			return K * LCMUtil(
						Num1 / K, Num2 / K, 2);
		}

		// Otherwise
		else
			return LCMUtil(Num1, Num2, K + 1);
	}

	// If K exceeds minimum
	else
		return Num1 * Num2;
}

// Function to calculate LCM
// of two numbers
void LCM(int N, int M)
{
	// Stores LCM of two number
	int lcm = LCMUtil(N, M, 2);

	// Print LCM
	printf("%d", lcm);
}

// Driver Code
int main()
{
	// Given N & M
	int N = 2, M = 4;

	// Function Call
	LCM(N, M);

	return 0;
}
