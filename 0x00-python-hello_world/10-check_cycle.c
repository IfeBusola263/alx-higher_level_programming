#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks for loop in linked list
 * @list: head pointer to linked list
 *
 * Return: 0 if none, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *tort, *hare;

	if (list != NULL)
	{
		tort = list;
		hare = list;

		while (hare->next && hare && hare->next->next)
		{
			hare = hare->next->next;
			tort = tort->next;
			if (hare == tort)
			{
				return (1);
			}
		}
		return (0);
	}
	return (0);
}
