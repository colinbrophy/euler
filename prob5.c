#include<stdio.h>


int main()
{
	int n = 20;
	int found = 0;
	int i;

	while(!found) {
		n++;
		found = 1;
		for (i = 2; i <= 20; i++)
		   if (n % i != 0) {
			   found = 0;
			   break;
		   }
	}
	printf("%d\n",n);
}
