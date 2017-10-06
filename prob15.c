#include <stdio.h>

static int total = 0;

static void walk_grid(int x, int y)
{
	/*printf("%d, %d\n", x, y);*/
	if (x == 20 && y == 20)
		total++;
	if (x != 20)
		walk_grid(x + 1, y);
	if (y != 20)
		walk_grid(x, y + 1);
}

int main(void)
{
	walk_grid(0, 0);
	printf("%d\n", total);
}
