#include <stdlib.h>
#include <stdio.h>
#include <stdio.h>
#include <unistd.h>

/**
* infinite_while - create infinite loop
* Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - creat 5 zombies and display their PID
* Return: 0
*/
int main(void)
{
	pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie <= 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
