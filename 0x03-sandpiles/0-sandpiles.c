#include "sandpiles.h"

/**
 * my_print_grid - Prints the grid
 * @grid: The grid to print
 */
void my_print_grid(int grid[3][3])
{
	int i = 0, j = 0;

	printf("=\n");

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d", grid[i][j]);
			if (j < 2)
				putchar(' ');
		}
		putchar('\n');
	}
}

/**
 * topple_grid - Takes care of the toppling that would occur
 * @grid: The grid in where the toppling is occurring
 * @toppleLocations: Specifically where the toppling is occurring
 */
void topple_grid(int grid[3][3], int toppleLocations[3][3])
{
	int i = 0, j = 0;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (toppleLocations[i][j] == 1)
			{
				grid[i][j] = grid[i][j] - 4;
				if (i > 0)
					grid[i - 1][j] = grid[i - 1][j] + 1;
				if (i < 2)
					grid[i + 1][j] = grid[i + 1][j] + 1;
				if (j > 0)
					grid[i][j - 1] = grid[i][j - 1] + 1;
				if (j < 2)
					grid[i][j + 1] = grid[i][j + 1] + 1;
			}
		}
	}
}

/**
 * sandpiles_sum - Computes sum of two sandpiles
 * @grid1: The first grid to add, where new grid will be saved
 * @grid2: The second grid to add
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i = 0, j = 0, flag = 0;
	int toppleLocations[3][3] = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};

	for (i = 0; i < 3; i++)
		for (j = 0; j < 3; j++)
			grid1[i][j] = grid1[i][j] + grid2[i][j];

	while (1)
	{
		flag = 0;

		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				if (grid1[i][j] > 3)
				{
					toppleLocations[i][j] = 1;
					flag = 1;
				}
				else
				{
					toppleLocations[i][j] = 0;
				}
			}
		}

		if (flag == 0)
			return;

		my_print_grid(grid1);

		topple_grid(grid1, toppleLocations);
	}
}