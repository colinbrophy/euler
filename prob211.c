#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MAXNO 64000000

static int perfect_sq(double n)
{
	double root = (long int) sqrt(n);
	return n == root * root;
}

long int sumsqdiv[MAXNO];

double sumgeoseries(double a, int n)
{
	/* sum of r= 0 to n a^(2r) */
	return (pow(a, 2*n + 2) - 1) / (a*a - 1);
}

void init_sumsqdiv(void)
{
	long int x,y;
	sumsqdiv[1] = 1;
	for (x = 2; x < MAXNO; x++) {
		int prime = 1;
		for (y = 2; y < sqrt(x); y++) {
			int power = 0;
			long int n = x;
			while (n % y == 0) {
				n /= y;
				power++;
			}
			if (power != 0) {
				sumsqdiv[x] = sumgeoseries(y, power) * sumsqdiv[n];
				prime = 0;
				break;
			}
		}
		if (prime)
			sumsqdiv[x] = x*x + 1;
	}
}

int main(void)
{
	long int total = 0;
	int i;

	init_sumsqdiv();
	for (i = 1; i < MAXNO; i++) {
		if (perfect_sq(sumsqdiv[i]))
			total += i;
	}

	printf("%ld\n", total);
}
