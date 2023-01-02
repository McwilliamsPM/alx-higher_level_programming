#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * list - linked list
 *
 * Return: 0 if cycle, 1 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *autobot, *decepticon;

	autobot = list;
	decepticon = list;

	while (autobot && decepticon)
	{
		if (decepticon->next == NULL)
			return (0);
		autobot = autobot->next;
		decepticon = decepticon->next->next;
		if (autobot == decepticon)
			return (1);
	}

	return (0);
}
