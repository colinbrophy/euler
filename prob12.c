#include <stdio.h>

int no_divisors(int n)
{
	int i;
	int divisors = 2; /* 1 and itself */

	for (i = 2; i < n; i++)
		if (n % i == 0)
			divisors++;

	return divisors;
}

int main(void)
{
	int trino = 1;
	int trino_index = 1;
	int divisors;

	/* printf("%d \n", no_divisors(4)); */

	while((divisors = no_divisors(trino)) < 500) {
		trino_index++;
		trino += trino_index;
	}
	printf("%d %d \n",trino, divisors);
}
