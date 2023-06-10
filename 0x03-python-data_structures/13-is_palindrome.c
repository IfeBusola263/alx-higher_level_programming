#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: a pointer to the head pointer
 *
 * Return: returns 1 at success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int arr[30], i, len;

	if (head != NULL)
	{
		ptr = *head;

		i = 0;
		while (ptr)
		{
			arr[i] = ptr->n;
			ptr = ptr->next;
			i++;
		}
		len = i;

		for (i = 0; i < len / 2; i++)
		{
			if (arr[i] != arr[len - i - 1])
				return (0);
		}
		return (1);
	}
	return (0);
}
